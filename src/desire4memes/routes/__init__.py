from flask import Blueprint

core_bp = Blueprint("core", __name__)
auth_bp = Blueprint("auth", __name__)

from desire4memes.routes import core, auth