from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(63), nullable=False, unique=True)
    password = db.Column(db.String(127), nullable=False)
    first_name = db.Column(db.String(63))
    last_name = db.Column(db.String(63))
    email = db.Column(db.String(63), unique=True)
    phone = db.Column(db.Integer, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)

    image = db.Column(db.String(127), default='user.jpg')

    def __repr__(self):
        return f'<User {self.name}>'
