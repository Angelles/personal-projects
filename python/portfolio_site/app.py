from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('app.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')