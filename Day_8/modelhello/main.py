#!/usr/bin/env python
from google.appengine.ext import ndb
import datetime
import webapp2
import jinja2
import logging
import os

class Student(ndb.Model):
    name = ndb.StringProperty(required = True)
    school = ndb.StringProperty(required = True)
    club = ndb.StringProperty(required = False)
    attended_cssi = ndb.BooleanProperty(required=False)
    created_date = ndb.DateProperty(required = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #student = Student(name = "Frank the Skank", school = "UC Irvine", club = "strip")
        template = jinja_environment.get_template("templates/index.html")
        self.response.write(template.render())
        #puts object into database lol
        #student.put()
        #self.response.write('Hello world!')
class AddStudentHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/addstudent.html")
        self.response.write(template.render())

class StudentCreateHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        school = self.request.get('school')
        club = self.request.get('club')
        attended_cssi = self.request.get('attended_cssi')
        current_date = datetime.datetime.now().date()
        if (attended_cssi == 'on'):
            attended_cssi_bool = True
        else:
            attended_cssi_bool = False
        logging.info('ATTENDED_CSSI: ' + attended_cssi)
        student = Student(name = name, school = school, club = club,
        attended_cssi = attended_cssi_bool, created_date = current_date)
        #student.created_date = current_date
        student.put()
        self.response.write('Student was created! Thanks bruh')
        self.response.write('<a href = "/addstudent">Add Student </a>')

class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        query = Student.query()
        student_data = query.fetch()
        #for student in student_data:
        #names.append(student.name)
        #logging.info(student_data)
        template_vars = {'students':student_data}
        template = jinja_environment.get_template("templates/list_students.html")
        self.response.write(template.render(template_vars))

class StudentViewHandler(webapp2.RequestHandler):
    def get(self):
        student_id = self.request.get('student_id')
        #logging.info("ID: " + student_id)
        student = Student.get_by_id(int(student_id))
        template_vars = {'student': student}
        template = jinja_environment.get_template("templates/view_student.html")
        self.response.write(template.render(template_vars))

jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/addstudent', AddStudentHandler),
    ('/student/create', StudentCreateHandler),
    ('/student/list', StudentListHandler),
    ('/student/view', StudentViewHandler)
], debug=True)
