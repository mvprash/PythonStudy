from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),unique=True,nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)
    password=db.Column(db.String(150),nullable=False)
    workouts=db.relationship('Workout',backref='author',lazy=True)

class Workout(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pushups=db.Column(db.Integer,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    comments=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    