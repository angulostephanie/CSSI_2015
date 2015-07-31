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
from google.appengine.api import users
import webapp2
import jinja2
import os


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href = %s>sign_out</a>)' %
            (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href ="%s">Sign in or register</a>.'%
            users.create_login_url('/login'))
            ##
        self.response.write('<html><body>%s</body></html>' % greeting)

class MainHandler(webapp2.RequestHandler):
        entry = JINJA_ENVIRONMENT.get_template('templates/entry.html')
        self.response.write(entry.render())

class ResponseHandler(webapp2.RequestHandler):
    def post(self):
        team_members = {'Frank the skank': {'college':'UC Irvine'},
                        'Steph the Deaf': {'college':'Occidental'},
                        'Tio Leo':{'college':'UC Irvine'},
                        'Yelena la Gringa':{'college':'Stanford'},
                        'Eleanor from Paramore':{'college':'CalPoly Slo'}}
        noun1 = self.request.get('noun1')
        adjective1 =self.request.get('adjective1')
        place1 = self.request.get('place1')
        verbEd1 =self.request.get('verbEd1')
        historicalmonument1 =self.request.get('historicalmonument1')
        verbEd2 = self.request.get('verbEd2')
        adjective2 =self.request.get('adjective2')
        animal =self.request.get('animal')
        vehicle = self.request.get('vehicle')
        historicalmonument2 =self.request.get('historicalmonument2')
        noun2 =self.request.get('noun2')
        name = self.request.get('name')
        bodypart =self.request.get('bodypart')
        onomatopoeia =self.request.get('onomatopoeia')
        adjective3= self.request.get('adjective3')

        dict_words = {'noun1':noun1,
                    'adjective1':adjective1,
                    'place1':place1,
                    'verbEd1':verbEd1,
                    'historicalmonument1':historicalmonument1,
                    'verbEd2':verbEd2,
                    'adjective2':adjective2,
                    'animal':animal,
                    'vehicle':vehicle,
                    'historicalmonument2':historicalmonument2,
                    'noun2':noun2, 'name':name,
                    'bodypart':bodypart,
                    'onomatopoeia':onomatopoeia,
                    'adjective3':adjective3,
                    'team_members': team_members}
        page= JINJA_ENVIRONMENT.get_template('templates/response.html')
        self.response.write(page.render(dict_words))

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape = True)


app = webapp2.WSGIApplication([
    ('/login', LoginHandler),
    ('/', MainHandler),
    ('/response', ResponseHandler)
], debug=True)
