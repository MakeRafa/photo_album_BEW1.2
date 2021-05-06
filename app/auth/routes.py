from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app.models import User, Album, Photo
from app.auth.forms import SignUpForm, LoginForm

from app import app, db, bcrypt

auth = Blueprint('auth', __name__)

# Create your routes here.

def signup():
    form = SignUpForm
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )