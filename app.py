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
	error = None
	results = None
	if request.method == 'POST':
		try:
			name=request.form.get('name',None)
			email=request.form.get('email',None)

			if email:
				person=Subscriber(
					email=email,
					name=name,
					is_subscribed=False
				)
				db.session.add(person)
				db.session.commit()
				results = '{} has been sent a confirmation email.'.format(person.email)
			else:
				error = "Email is required."
		except:
			error = "Error creating subscriber."

	return render_template("subscribe.html", error=error, results=results)

@app.route("/unsubscribe")
def unsubscribe(email):
	error=None
	results=None
	if request.method == 'POST':
		try:
			person = Subscriber.query.filter_by(email=email).first()
			results = '{} as been unsubscribed.'.format(person.email)
			db.session.delete(person)
			db.session.commit()
		except:
			error = "Could not find that email."

	return render_template("unsubscribe.html", error=error, results=results)

@app.route("/confirm/<id>")
def confirm(id):
    return "Confirmed"

if __name__ == '__main__':
    app.run()
