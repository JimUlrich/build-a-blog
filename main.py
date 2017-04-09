import webapp2
import jinja2
import os

from google.appengine.ext import db
# set up jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.redirect("/blog")


#create class for database
#create blog page
#create page for submitting posts


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', Blog)
], debug=True)
