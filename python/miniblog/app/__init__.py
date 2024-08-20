from flask import Flask

app = Flask(__name__)

@app.get("/login")
def login_get():
    return show_the_login_form()

@app.post("/login")
def login_post():
    return do_the_login()

from app import routes