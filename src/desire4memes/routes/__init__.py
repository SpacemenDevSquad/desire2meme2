def register_routes(app):
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .core import core_bp
    app.register_blueprint(core_bp)
