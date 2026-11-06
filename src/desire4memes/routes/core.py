from typing import cast, Any, Dict
import json

from flask import render_template, redirect, flash, url_for, Blueprint
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from desire4memes.queries import get_recent_memes, get_oldest_memes
from desire4memes.forms import MemeForm
from desire4memes.models import Meme
from desire4memes.extensions import db, lm
from desire4memes.routes import is_logged_in

core_bp = Blueprint("core", __name__)

@core_bp.get("/")
def get_index():
    return redirect(url_for("core.get_home"))

@core_bp.get("/home")
def get_home():
    return render_template("home.html", user = (None if not is_logged_in() else current_user), memes = get_recent_memes())

@core_bp.get("/home/oldest")
def get_home_oldest():
    return render_template("home.html", user = (None if not is_logged_in() else current_user), memes = get_oldest_memes())

@core_bp.get("/create")
@login_required
def get_create_meme():
    form = MemeForm()
    return render_template("create_meme.html", user = (None if not is_logged_in() else current_user), form = form)

@core_bp.post("/create")
@login_required
def post_create_meme():
    form = MemeForm()

    if form.validate():
        try:
            title: str = cast(str, form.title.data)
            image: bytes = cast(bytes, form.image.data)

            ##################################################
            # TODO: Figure out how file types should be stored
            ##################################################

            temp_fabric: str | None = cast(str, form.fabric.data)

            fabric: Dict[str, Any] | None = None
            if temp_fabric is not None:
                fabric = json.loads(temp_fabric)

            caption: str | None = cast(str, form.caption.data)
    
            assert title is not None and image is not None

            new_meme: Meme = Meme(user_id = current_user.username, title = title, image = image, fabric = fabric, caption = caption)
    
            db.session.add(new_meme)
            db.session.commit()
    
            return redirect(url_for("core.get_home")),
            
        except IntegrityError:
            flash("Database Issue")
            db.session.rollback()
    
    for field, errors in form.errors.items():
        for msg in errors:
            flash(f"{field}: {msg}")
    
    return render_template("create_meme.html", user = (None if not is_logged_in() else current_user), form = form), 422

@core_bp.get("/account")
@login_required
def get_account():
    return render_template("account.html", user = (None if not is_logged_in() else current_user))

@core_bp.get("/settings")
@login_required
def get_settings():
    return render_template("settings.html", user = (None if not is_logged_in() else current_user))