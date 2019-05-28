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

def importer(sierraApiCall):
    #script a Sierra api or sql query call to get records changed in the last X days
    while sierraApiCall:
        #slice into batches of 50 and call batchSet(csvBatch) below

        # data = numpy.loadtxt(open('data/sandboxRecords.csv'), delimiter='/n',dtype='int')
        # #need to loop through more than fifty or entire csv
        # test = list(data[:50])
        #base url plus url encode csv converting commas to %20
        batchSet(fifty)

def batchSet(csvBatch): # where batch is csv list of oclc numbers
    import requests, json
    import stati.get_token
    from stati.get_token import my_wskey, my_user

    import csv, stati.holdingStatus, re, numpy, urllib, stati.setHolding, stati.unsetHolding
    from stati.unsetHolding import unset
    from stati.setHolding import set
    from stati.holdingStatus import status

    stringBatch = ''
    for i in csvBatch: # parsing sqlite3 return array of oclc numbers
        test += str(i)[0]+',' # for altering input array formats use test += str(i)+','
    try:
        urllib.parse.quote(stringBatch)
        url = 'https://worldcat.org/ih/datalist?holdingLibraryCode=MIA&oclcNumbers='+urllib.parse.quote(stringBatch)
    except:
        print('URL Encode failed. Check list of oclc numbers')

    authorization_header = my_wskey.get_hmac_signature(
        method='POST',
        request_url=url,
        options={
            'user': my_user,
            'auth_params': None}
    )

    headers={'Authorization': authorization_header, 'Accept':'application/atom+json; charset=utf8'}
    try:
        r = requests.post(url, headers=headers)
        r.raise_for_status()
        return json.loads(r.content)
    except requests.exceptions.HTTPError as err:
        print("Read failed. " + str(err.response.status_code))

# parse the response of batchSet()
def responseParse(r):
    import json # status 
    # parse r json conent looking for status codes other than 409 and 200
    # parse response of batch api
    for i in r['entries']:
        #check to make sure oclcnumber is correct length
        #number errors out; does not like str action on numpy bytes object
        #test for bytes: number = re.sub(b"[^0-9]",b"",b"{}".format(data[0]))
        if i['content']['status'] == 'HTTP 200 OK':
            # add column to sqlite database noting status updated date
            print('all good')
        else:
            try:
                number = re.sub("[^0-9]","",str(i['content']['requestedOclcNumber'])) #takes out any characters
                if number == i:
                    print('number has no chars')
                else:
                    print('number had chars, trying again without chars')
                    try:
                        set(number) # retry
                        print('retry worked')
                    except:
                        print('retry failed. add number '+number+'to error list')

            except:
                print('towel thrown')
        #try to set status from error response object
        # if holding == False:
        #     print(s,number,holding,set(number)) #dev testing vars
    print("Finished")
