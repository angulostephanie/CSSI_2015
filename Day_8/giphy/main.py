#!/usr/bin/env python

import webapp2
import urllib2
import json
import jinja2
import os

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class PugHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('gifs.html')
        url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=funny+pugs"
        string = urllib2.urlopen(url)
        bigdictionary =json.loads(string.read())
        pug_url = bigdictionary['data']['image_url']
        template_vars = {'pug_url':pug_url}
        self.response.write(template.render(template_vars))

JINJA_ENVIRONMENT = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pugs', PugHandler)
], debug=True)
