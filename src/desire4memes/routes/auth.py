from flask import render_template, session, flash, redirect, url_for

from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required

from desire4memes.routes import auth_bp
from desire4memes.forms import SignUpForm, LoginForm
from desire4memes.extensions import db
from desire4memes.models import User, Post

# TODO: Implement Argon, password hashing, salting, and peppering

@auth_bp.get("/signup")
def get_signup_form():
    form = SignUpForm()
    return render_template("signup.html", form = form)

@auth_bp.post("/signup")
def post_signup_form():
    form = SignUpForm()

    if form.validate():
        username: str|None = form.name.data
        password: int|None = form.number.data

        assert username is not None and password is not None
        session["username"] = username

        return redirect(url_for("auth.get_login_form"))

@auth_bp.get("/login")
def get_login_form():
    form = LoginForm()
    return render_template("login.html", form = form)

@auth_bp.post("/login")
def post_login_form():
    form = LoginForm()

    if form.validate():
        username: str|None = form.name.data
        password: int|None = form.number.data

        assert username is not None and password is not None
        session["username"] = username

        login_user(username)
        return redirect(url_for("core.get_feed"))

@auth_bp.get("/logout")
@login_required
def get_logout():
    logout_user()
    return redirect(url_for("get_home"))