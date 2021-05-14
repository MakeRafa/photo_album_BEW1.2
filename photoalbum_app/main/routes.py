from os import name
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from photoalbum_app import app, db

from photoalbum_app.main.forms import AlbumForm, PhotoForm
from photoalbum_app.models import Album, Photo

main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def homepage():
    all_albums = Album.query.all()
    return render_template('home.html', all_albums=all_albums)

@main.route('/create_album', methods=['GET', 'POST'])
@login_required
def create_album():
    form = AlbumForm()

    if form.validate_on_submit():
        new_album = Album(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(new_album)
        
        db.session.commit()
        flash('Your new album has been added!')

        return redirect(url_for('main.homepage', album_id=new_album.id))
    return render_template('create_album.html', form=form)

@main.route('/album/<album_id>', methods=['GET', 'POST'])
@login_required
def album_info(album_id):
    album = Album.query.get(album_id)

    form = AlbumForm(obj=album)

    if form.validate_on_submit():
        album.title = form.title.data
        album.description = form.description.data

        db.session.commit()
        flash('Your Album has been updated!')

        return redirect(url_for('main.homepage', album_id=album.id))        
    return render_template('album_info.html', album=album, form=form)

@main.route('/create_photo', methods=['GET', 'POST'])
@login_required
def create_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        new_photo = Photo(
            name=form.name.data,
            photo_url=form.photo_url.data,
            location=form.location.data,
            date=form.date.data,
            album=form.album.data,
            small_description=form.small_description.data
        )
        db.session.add(new_photo)
        db.session.commit()

        flash('Photo has been added to the designated album')
        
        return redirect(url_for('main.homepage', photo_id=new_photo.id))
    return render_template('create_photo.html', form=form)

@main.route('/photo/<photo_id>', methods=['POST', 'GET'])
@login_required
def photo_info(photo_id):
    photo = Photo.query.get(photo_id)

    form = PhotoForm(obj=photo)

    if form.validate_on_submit():
        photo.name = form.name.data
        photo.photo_url = form.photo_url.data
        photo.location = form.location.data
        photo.date = form.date.data
        photo.album = form.album.data
        photo.small_description = form.small_description.data

        db.session.commit()
        flash('Your photo has been successfully updated')

        return redirect(url_for('main.photo_info', photo_id=photo.id))        
    return render_template('photo_info.html', photo=photo, form=form)