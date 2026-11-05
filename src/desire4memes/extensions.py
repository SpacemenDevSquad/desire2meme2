from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from desire4memes.authentication import Hasher

db = SQLAlchemy()
lm = LoginManager()
hasher = Hasher


def InitializeLoginManager(LoginManager: LoginManager, app: Flask):
    LoginManager.init_app(app)
    LoginManager.session_protection = "strong"

    from desire4memes.models import User
    @LoginManager.user_loader
    def load_user(uid: str) -> User | None:
        return get_user(uid=int(uid))

    #TODO: Implement get_user()
    def get_user(uid: int | None):
        return User()

def InitializeDatabase(database: SQLAlchemy, app: Flask):
    database.init_app(app)
    with app.app_context():
        database.create_all()
