from sqlalchemy_utils import URLType

from sqlalchemy.orm import backref

from flask_login import UserMixin

from app import db
from photoalbum_app.utils import FormEnum
# Create your models here.
class User(UserMixin, db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class Album(db.Model):
    """Album Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    # photos = db.relationship()

class Photo(db.Model):
    """Photo Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    small_description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

