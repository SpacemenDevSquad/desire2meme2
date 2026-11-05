from __future__ import annotations

from typing import Any

def create_app(config: Any = None):
    from flask import Flask
    app = Flask(__name__)

    if config is None:
        from desire4memes.config import get_config
        config = get_config()
    
    app.config.from_object(config)

    from desire4memes.extensions import db
    db.init_app(app)

    from desire4memes.extensions import lm
    lm.init_app(app)

    from desire4memes.routes import core_bp, auth_bp

    app.register_blueprint(core_bp, url_prefix = "")
    app.register_blueprint(auth_bp, url_prefix = "")

    with app.app_context():
        db.create_all()

    return app