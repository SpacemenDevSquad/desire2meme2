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

    with app.app_context():
        db.create_all()

    from desire4memes.routes import register_routes
    register_routes(app)

    return app