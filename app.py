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
def unsubscribe(email):
	c = {}
	c.update({'error':None})
	c.update({'results':None})
	if request.method == 'POST':
		try:
			person = Subscriber.query.filter_by(email=email).first()
			c['results'] = '{} as been unsubscribed.'.format(person.email)
			db.session.delete(person)
			db.session.commit()
		except:
			error = "Could not find that email."

	return render_template("unsubscribe.html", c)

@app.route("/confirm/<id>")
def confirm(id):
    return "Confirmed"

if __name__ == '__main__':
    app.run()
