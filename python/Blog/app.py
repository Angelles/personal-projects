import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

###
# Per DigitalOcean:
# This get_db_connection() function opens a connection to the database.db database file, and then sets the row_factory
# attribute to sqlite3.Row so you can have name-based access to columns. This means that the database connection will
# return rows that behave like regular Python dictionaries. Lastly, the function returns the conn connection object
# you’ll be using to access the database.
# See https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3 for more
# details.
###


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Get all posts and display them on the index page using the template.
@app.route('/')
def index():
    conn = get_db_connection()  # Open the db connection.
    posts = conn.execute('SELECT * FROM posts').fetchall()  # Get all the rows of posts.
    conn.close()  # Close the connection.
    return render_template('index.html', posts=posts)


# Get individual post.
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
