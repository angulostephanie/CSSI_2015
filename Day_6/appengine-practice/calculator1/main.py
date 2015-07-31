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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('templates/calc.html')

        self.response.write(template.render())

class MathHandler(webapp2.RequestHandler):
    def get(self):
        firstnum = self.request.GET['firstnum']
        secondnum = self.request.GET['secondnum']
        operation = self.request.get('operation')
        if operation == 'add':
            self.response.write(firstnum)
            self.response.write(' + ')
            self.response.write(secondnum)
            self.response.write(' = ')
            self.response.write(float(firstnum) + float(secondnum))
        if operation == 'subtract':
            self.response.write(firstnum)
            self.response.write(' - ')
            self.response.write(secondnum)
            self.response.write(' = ')
            self.response.write(float(firstnum) - float(secondnum))
        if operation == 'multiply':
            self.response.write(firstnum)
            self.response.write(' x ')
            self.response.write(secondnum)
            self.response.write(' = ')
            self.response.write(float(firstnum) * float(secondnum))
        if operation == 'divide':
            self.response.write(firstnum)
            self.response.write(' / ')
            self.response.write(secondnum)
            self.response.write(' = ')
            self.response.write(float(firstnum) / float(secondnum))

jinja2_environment = jinja2.Environment(loader =
jinja2.FileSystemLoader(os.path.dirname(__file__)))
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/math', MathHandler),
], debug=True)
