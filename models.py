from app import db
import datetime

class Subscriber(db.Model):
    __tablename__ = 'subscriber'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    name = db.Column(db.String())
    is_confirmed = db.Column(db.Boolean())
    date_confirmed = db.Column(db.DateTime())

    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.is_confirmed = False

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def set_confirmed(self, name):
        self.is_confirmed = True
        self.date_confirmed = datetime.datetime.now()
