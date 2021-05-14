from sqlalchemy_utils import URLType

from flask_login import UserMixin

from photoalbum_app import db
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

    """ Relationship """
    photos = db.relationship('Photo', back_populates='album')

    """ Relationship """
    created_by = db.relationship('User')

    """Foreign Key"""
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Photo(db.Model):
    """Photo Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    small_description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(URLType)

    ##########################################
    #     User Relationship/Foreign Key      #
    ##########################################

    """ Relationship """
    created_by = db.relationship('User')

    """Foreign Key"""
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    ##########################################
    #    Album Relationship/Foreign Key      #
    ##########################################
    """Foreign Key"""
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    """Relationship"""
    album = db.relationship('Album', back_populates='photos')
    
