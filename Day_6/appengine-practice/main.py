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
import webapp2
import math
import logging
import jinja2
import os
import time

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars ={
        'timeofday': time.asctime()
        'filepath':os.path.dirname(__file__)
        }
        template = jinja2_environment.get_template('templates_copy/hello.html')
        self.response.write(template.render(template_vars))
        #self.response.write('<a href = "add?firstnum=30&secondnum=6">Do math with numbers 30 and 6<a/a>')
        self.response.write('<br/>')
        self.response.write('I hate mondays')

class FormHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        self.response.writer('Thanks '+ name)



        #logging.warning(' FIRSTNUM = ' + firstnum)

jinja2_environment = jinja2.Environment(loader =
jinja2.FileSystemLoader(os.path.dirname(__file__)))
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler)
], debug=True)

#
