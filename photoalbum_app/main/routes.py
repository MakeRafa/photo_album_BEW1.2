from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from datetime import date, datetime

from photoalbum_app import app, db, bcrypt

from photoalbum_app.main.forms import AlbumForm, PhotoForm
main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def homepage():
    pass

@main.route('/create_album')
def create_album():
    form = AlbumForm()

    if form.validate_on_submit():
        # create new Album and direct user to add info
        new_album = AlbumForm(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(new_album)
        db.session.commit()
        flash('Your new album has been added!')

        return redirect(url_for())