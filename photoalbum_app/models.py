from sqlalchemy_utils import URLType

from sqlalchemy.orm import backref

from flask_login import UserMixin

from app import db
from app.utils import FormEnum
# Create your models here.
class User:
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class Album:
    """Album Model"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    # photos = db.relationship()

class Photo:
    """Photo Model"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    small_description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

