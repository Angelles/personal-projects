from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
