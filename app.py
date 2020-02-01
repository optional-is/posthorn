from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
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
