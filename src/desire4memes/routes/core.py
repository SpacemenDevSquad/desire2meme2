from flask import render_template, session, flash, redirect, url_for
from desire4memes.routes import core_bp

@core_bp.get('/')
def get_index():
    return # render_template("index.html")