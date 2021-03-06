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
import jinja2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./HTML'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class singleHandler(webapp2.RequestHandler):
    def get(self, fromhome):
        try:
            template = JINJA_ENVIRONMENT.get_template(str(fromhome)+'.html')
            self.response.write(template.render({}))
        except:
            template = JINJA_ENVIRONMENT.get_template('error.html')
            self.response.write(template.render({}))

class mainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

class topicHandler(webapp2.RequestHandler):
    def get(self,topics,topic):
        try:
            template = JINJA_ENVIRONMENT.get_template(str(topic)+'.html')
            self.response.write(template.render({}))
        except:
            template = JINJA_ENVIRONMENT.get_template('error.html')
            self.response.write(template.render({}))

class NotFoundPageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('error.html')
        self.response.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/', mainHandler),
    webapp2.Route(r'/<fromhome>',
                  handler=singleHandler),
    webapp2.Route(r'/<topics>/<topic>',
                  handler=topicHandler),
    ('/.*', NotFoundPageHandler)
], debug=True)
