#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ###############################################################################
# Copyright Miami University Libraries - Craig Boman
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################


#purpose: sets the status for fifty items from csv

def batchSet():
    import requests, json
    import get_token
    from get_token import my_wskey, my_user

    import csv, holdingStatus, re, numpy, urllib
    from unsetHolding import unset
    from setHolding import set
    from holdingStatus import status

    data = numpy.loadtxt(open('../data/sandboxRecords.csv'), delimiter='/n',dtype='int')
    #need to loop through more than fifty or entire csv
    test = list(data[:50])
    #base url plus url encode csv converting commas to %20
    url = 'https://worldcat.org/ih/datalist?holdingLibraryCode=MIA&oclcNumbers='+urllib.parse.quote(test)

    authorization_header = my_wskey.get_hmac_signature(
        method='POST',
        request_url=request_url,
        options={
            'user': my_user,
            'auth_params': None}
    )

    headers={'Authorization': authorization_header, 'Accept':'application/atom+json; charset=utf8'}
    try:
        r = requests.post(request_url, headers=headers)
        r.raise_for_status()
        return json.loads(r.content)
    except requests.exceptions.HTTPError as err:
        print("Read failed. " + str(err.response.status_code))

#parse the response of batchSet()
def responseParse(r):

    #parse r json conent looking for status codes other than 409 and 200

    #use to parse response of batch api
    for i in r:
        for s in range(len(data)):
            #check to make sure oclcnumber is correct length
            #number errors out; does not like str action on numpy bytes object
            #test for bytes: number = re.sub(b"[^0-9]",b"",b"{}".format(data[0]))
            number = re.sub("[^0-9]","",str(data[s])) #takes out any characters
            #if len(number) !=
            holding = status(number)
            #try to set status from error response object
            if holding == False:
                print(s,number,holding,set(number)) #dev testing vars
            #else:
                #nothing
        if s == len(data)-1:
            break
    print("stop")
