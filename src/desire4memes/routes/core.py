from typing import cast, Any, Dict
import json

from flask import render_template, session, redirect, flash, url_for, Blueprint
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from desire4memes.queries import get_recent_memes, get_oldest_memes
from desire4memes.forms import MemeForm
from desire4memes.models import Meme
from desire4memes.extensions import db, lm

core_bp = Blueprint("core", __name__)

@core_bp.get("/")
def get_index():
    username: str | None = session.get("username")
    return render_template("landing.html")

@core_bp.get("/home")
def get_home():
    return render_template("landing.html", username = (current_user if current_user is not None else "Anon"), memes = get_recent_memes())

@core_bp.get("/home/oldest")
def get_home_oldest():
    return render_template("landing.html", username = (current_user if current_user is not None else "Anon"), memes = get_oldest_memes())

@core_bp.get("/create")
@login_required
def get_create_meme():
    form = MemeForm()
    return render_template("create_meme.html", form = form)

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

            new_meme: Meme = Meme(user_id = current_user, title = title, image = image, fabric = fabric, caption = caption)
    
            db.session.add(new_meme)
            db.session.commit()
    
            return redirect(url_for("core.get_home")),
            
        except IntegrityError:
            flash("Database Issue")
            db.session.rollback()
    
    for field, errors in form.errors.items():
        for msg in errors:
            flash(f"{field}: {msg}")
    
    return render_template("create_meme.html", form = form), 422

@core_bp.get("/account")
@login_required
def get_account():
    return render_template("acount.html")

@core_bp.get("/settings")
@login_required
def get_settings():
    return render_template("settings.html")