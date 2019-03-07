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


#purpose: loop through csv list of records

def loopHolding():
    import csv, holdingStatus, re
    from holdingStatus import status

    with open('../data/sandboxRecords.csv') as file:
        data = list(csv.reader(file))

    for i in data:
        for s in range(len(data)):
            #check to make sure oclcnumber is correct length
            number = re.sub("[^0-9]","",data[s][0]) #takes out any characters
            #if len(number) !=
            holding = status(number)
            #if holding = False:
                #updateHolding(number)
            #elif holding = True:
                #Something
            #else:
                #nothing
            print(s,number,holding) #dev testing variables
        if s == len(data)-1:
            break
    print("stop")
