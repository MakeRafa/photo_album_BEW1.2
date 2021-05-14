from flask import Blueprint, render_template, redirect, url_for, flash

from photoalbum_app import app, db

from photoalbum_app.main.forms import AlbumForm, PhotoForm
from photoalbum_app.models import Album, Photo

main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def homepage():
    all_albums = Album.query.all()
    return render_template('home.html', all_albums=all_albums)

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

        return redirect(url_for('main.album_info', album_id=new_album.id))
    return render_template('create_album.html', form=form)

def album_info(album_id):
    album = Album.query.get(album_id)

    form = AlbumForm(obj=album)

    if form.validate_on_submit():
        album.title = form.title.data
        album.description = form.description.data

        db.session.commit()
        flash('Your Album has been updated!')

        return redirect(url_for('main.album_info', album_id=album.id))        
    return render_template('album_info.html', album=album, form=form)