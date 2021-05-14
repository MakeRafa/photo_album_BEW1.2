from photoalbum_app.models import Album
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

# Create your forms here.

class AlbumForm(FlaskForm):
    """Album Form for created new Albums"""
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=20)])
    description = StringField("Description", validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField("Submit")

class PhotoForm(FlaskForm):
    """Album Form for created new Albums"""
    name = StringField("Name", validators=[DataRequired(), Length(max=20)])
    photo_url = StringField("Photo URL", validators=[URL(require_tld=True)])
    location = StringField("Location", validators=[DataRequired(), Length(min=5, max=100)])
    date = DateField("Date", format= '%Y-%m-%d')
    small_description = StringField("Small Description", validators=[DataRequired(), Length(min=5, max=100)])
    album = QuerySelectField('Album', query_factory=lambda: Album.query, allow_blank=False)
    submit = SubmitField("Submit")