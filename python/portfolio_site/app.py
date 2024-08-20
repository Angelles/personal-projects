from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('app.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.get("/login")
def login_get():
    return show_the_login_form()

@app.post("/login")
def login_post():
    return do_the_login()

# view all blog posts. consider pagination.
@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/create")
def create():
    return render_template('create.html')

# this should cover deleting one or all posts
@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route("/update")
def update():
    return render_template('update.html')



