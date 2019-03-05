#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ###############################################################################
# Copyright 2014 OCLC
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

# Sample HMAC Hashing for Bibliographic record retrieval

from authliboclc import wskey, user
import requests
import xml.etree.ElementTree as ET

#
# You must supply these parameters to authenticate
# Note - a WSKey consists of two parts, a public clientID and a private secret
#

key = {key}
secret = {secret}
principal_id = {id}
principal_idns = {idns}
authenticating_institution_id = {inst_id}

my_wskey = wskey.Wskey(
    key=key,
    secret=secret,
    options=None)

my_user = user.User(
    authenticating_institution_id=authenticating_institution_id,
    principal_id=principal_id,
    principal_idns=principal_idns
)

