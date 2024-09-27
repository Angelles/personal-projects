from flask_mail import Message
from app import mail
from threading import Thread
from flask_babel import _
# import app.auth
from flask import current_app

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app.main, msg)).start()  # send_async email fn runs in background thread & is cleaned up when the process is complete