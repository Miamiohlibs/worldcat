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

# Retrieves status of individual OCLC number from your local/test collection
# Currently MIA is hardcoded; could replace with arg/kwarg variable if needed

def status(oclcNumb):
    import requests, json
    from stati.get_token import my_wskey, my_user

    request_url = 'https://worldcat.org/ih/checkholdings?holdingLibraryCode=MIA&oclcNumber='+oclcNumb

    authorization_header = my_wskey.get_hmac_signature(
        method='GET',
        request_url=request_url,
        options={
            'user': my_user,
            'auth_params': None}
    )

    headers={'Authorization': authorization_header, 'Accept':'application/atom+json; charset=utf8'}
    try:
        r = requests.get(request_url, headers=headers)
        r.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print("Read failed. " + str(err.response.status_code))

    #loads response into object;returns oclc number status
    return json.loads(r.content)["content"]["holdingCurrentlySet"]
