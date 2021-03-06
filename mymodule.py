#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import datetime
import userdb

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

def show_page(user_name):
    results = db.GqlQuery("SELECT * FROM Mydb WHERE name = :1", user_name)
    thehour=''
#    for result in results:
#        if result.push_time:
#            thehour = thehour+str(result.push_time.hour)+':'+str(result.push_time.minute)+':'+str(result.push_time.second)+'<br>'
        
    logout_url = users.create_logout_url("/")
    template_values = {'user_name' : user_name,
                        'logout_url' : logout_url,
                        'results' : results,
                       }
    path = os.path.join(os.path.dirname(__file__), 'static/template.html')
    return thehour+template.render(path, template_values)