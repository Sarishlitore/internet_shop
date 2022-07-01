from datetime import datetime

from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    psw = db.Column(db.String(128), nullable=False)

    profile = db.relationship('Profiles', backref='user', uselist=False)

    def __repr__(self):
        return f'<User {self.id}>'


class Profiles(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Profile {self.user_id}>'
