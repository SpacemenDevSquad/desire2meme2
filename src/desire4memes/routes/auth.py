from typing import cast

from flask import render_template, session, flash, redirect, url_for, Blueprint
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required

from desire4memes.forms import SignUpForm, LoginForm
from desire4memes.extensions import db, hasher
from desire4memes.models import User
from desire4memes.queries import get_user

###########################################################
# TODO: Fix Argon, password hashing, salting, and peppering
###########################################################

auth_bp = Blueprint("auth", __name__)

@auth_bp.get("/signup")
def get_signup_form():
    form = SignUpForm()
    return render_template("signup.html", form = form)

@auth_bp.post("/signup")
def post_signup_form():
    form = SignUpForm()

    if form.validate():
        try:
            username: str | None = cast(str, form.username.data)
            password: str | None = cast(str, form.password.data)

            assert username is not None and password is not None

            new_user: User = User(username = username, password = hasher.hash(password), is_admin = False)

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("auth.get_login_form")), 302
        
        except IntegrityError:
            flash("Database Issue")
            db.session.rollback()

    for field, errors in form.errors.items():
        for msg in errors:
            flash(f"{field}: {msg}")

    form.password.data = ""
    return render_template("signup.html", form = form), 422

@auth_bp.get("/login")
def get_login_form():
    form = LoginForm()
    return render_template("login.html", form = form)

@auth_bp.post("/login")
def post_login_form():
    form = LoginForm()

    if form.validate():
        username: str | None = cast(str, form.username.data)
        print(username)
        password: str | None = cast(str, form.password.data)

        assert username is not None and password is not None

        user: User | None = get_user(username)

        if user is not None:
            if hasher.check(password, user.password):
                login_user(user)
                return redirect(url_for("core.get_home")), 302
            else:
                flash("Incorrect Password")
        else:
            flash("User Not Found")

    for field, errors in form.errors.items():
            for msg in errors:
                flash(f"{field}: {msg}")

    return render_template("login.html", form = form), 422

@auth_bp.get("/logout")
@login_required
def get_logout():
    logout_user()
    return redirect(url_for("get_home"))