from __future__ import annotations

from typing import Any

def create_app(config: Any = None):
    from flask import Flask
    app = Flask(__name__)

    # Config options
    if config is None:
        from desire4memes.config import get_config
        config = get_config()
    
    app.config.from_object(config)

    # Setup db
    from desire4memes.extensions import db, InitializeDatabase
    InitializeDatabase(db, app)

    # Setup login
    from desire4memes.extensions import lm, InitializeLoginManager
    InitializeLoginManager(lm, app)

    # Register Routes
    from desire4memes.routes import register_routes
    register_routes(app)

    return app