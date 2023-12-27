from flask import Flask

app = Flask(__name__)


@app.route('/')
def application():
    return 'Hi, this is your app'
