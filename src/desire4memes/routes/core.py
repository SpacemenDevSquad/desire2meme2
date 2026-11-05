from flask import render_template, session, flash, redirect, url_for, Blueprint
from flask_login import login_required

from desire4memes.extensions import db, lm
from desire4memes.forms import CreateMemeForm

core_bp = Blueprint("core", __name__)

@core_bp.get("/")
def get_index():
    return redirect(url_for("core.get_home"))

@core_bp.get("/home")
def get_home():
    username: str | None = session.get("username")
    return render_template("landing.html")

@core_bp.get("/create")
@login_required
def get_create_meme():
    form = CreateMemeForm()
    return render_template("create_meme.html", form = form)

@core_bp.post("/create")
@login_required
def post_create_meme():
    form = CreateMemeForm()
    return redirect(url_for("/home"))

@core_bp.get("/settings")
@login_required
def get_settings():
    return render_template("settings.html")