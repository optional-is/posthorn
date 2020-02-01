from app import db

class Subscriber(db.Model):
    __tablename__ = 'subscriber'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    name = db.Column(db.String())
    is_confirmed = db.Column(db.Boolean())
    date_confirmed = db.Column(db.DateTime())

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'email': self.email
        }