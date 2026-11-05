from flask import render_template, session, redirect, url_for, Blueprint
from flask_login import login_required

from desire4memes.queries import get_recent_memes, get_oldest_memes
from desire4memes.forms import MemeForm

core_bp = Blueprint("core", __name__)

@core_bp.get("/")
def get_index():
    return redirect(url_for("get_home"))

@core_bp.get("/home")
def get_home():
    username: str | None = session.get("username")
    return render_template("home.html", username = username, memes = get_recent_memes())

@core_bp.get("/home/oldest")
def get_home_oldest():
    username: str | None = session.get("username")
    return render_template("home.html", username = username, memes = get_oldest_memes())

@core_bp.get("/create")
@login_required
def get_create_meme():
    form = MemeForm()
    return render_template("create_meme.html", form = form)

@core_bp.post("/create")
@login_required
def post_create_meme():
    form = MemeForm()
    return redirect(url_for("/home"))

@core_bp.get("/account")
@login_required
def get_account():
    return render_template("acount.html")

@core_bp.get("/settings")
@login_required
def get_settings():
    return render_template("settings.html")