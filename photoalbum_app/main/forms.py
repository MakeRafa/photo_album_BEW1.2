from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError

# Create your forms here.

class AlbumForm(FlaskForm):
    """Album Form for created new Albums"""
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=10)])
    description = StringField("Description", validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField("Submit")

class PhotoForm(FlaskForm):
    """Album Form for created new Albums"""
    name = StringField("Name", validators=[DataRequired(), Length(max=20)])
    location = StringField("Location", validators=[DataRequired(), Length(min=5, max=100)])
    date = DateField("Date")
    small_description = StringField("Small Description", validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField("Submit")