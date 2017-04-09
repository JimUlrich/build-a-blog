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

class Posts(db.Model):
    title =  db.StringProperty(required = True)
    post = db.TextProperty(required = True)
    created = created = db.DateTimeProperty(auto_now_add = True)


#create blog page
class Blog(webapp2.RequestHandler):

    def render_page(self, title="", post="", error=""):
        posts = db.GqlQuery("SELECT * FROM Posts "
                           "ORDER BY created DESC "
                           "LIMIT 5")
        t = jinja_env.get_template("blog.html")
        content = t.render(title=title, post=post, posts=posts)
        self.response.write(content)

    def get(self):
        self.render_page()

#create page for submitting posts
class NewPost(webapp2.RequestHandler):

    def render_page(self, title="", post="", error=""):
        t = jinja_env.get_template("newpost.html")
        content = t.render(title=title, post=post, error=error)
        self.response.write(content)

    def get(self):
        self.render_page()

    def post(self):
        title = self.request.get("title")
        post = self.request.get("post")

        if title and post:
            p = Posts(title = title, post = post)
            p.put()

            self.redirect("/blog")
        else:
            error = "Please fill out both fields"
            self.render_page(title, post, error)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', Blog),
    ('/blog/newpost', NewPost)
], debug=True)
