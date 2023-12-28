import sqlite3
from flask import Flask, render_template

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


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection() # Open the db connection.
    tasks = conn.execute('SELECT * FROM tasks').fetchall() # Get all the rows of tasks.
    conn.close() # Close the connection.
    return render_template('index.html', tasks=tasks)
