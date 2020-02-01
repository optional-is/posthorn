from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Subscriber

@app.route("/")
def subscribe():
    return "Hello World!"

@app.route("/unsubscribe/<id>")
def unsubscribe(id):
    return "name : {}".format(name)

@app.route("/confirm/<id>")
def confirm(id):
    return "Confirmed"

if __name__ == '__main__':
    app.run()
