from __future__ import annotations
from typing import Any

def create_wsgi_app(config: Any = None):
    from flask import Flask
    flask_app = Flask(__name__)

    if config is None:
        from desire4memes.config import get_config
        config = get_config()
    
    flask_app.config.from_object(config)

    #from desire4memes.routes import core_bp
    #flask_app.register_blueprint(core_bp, url_prefix = "")