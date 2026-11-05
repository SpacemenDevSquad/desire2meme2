from flask import Blueprint

core_bp = Blueprint("core", __name__)
auth_bp = Blueprint("auth", __name__)

import desire4memes.routes.core
import desire4memes.routes.auth