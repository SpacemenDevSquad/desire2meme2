from pathlib import Path

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from desire4memes.authentication import Hasher

db = SQLAlchemy()

def InitializeDatabase(database: SQLAlchemy, app: Flask):
    database.init_app(app)
    with app.app_context():
        from desire4memes.models import User, Meme

        database.create_all()

lm = LoginManager()

def InitializeLoginManager(LoginManager: LoginManager, app: Flask):
    LoginManager.init_app(app)
    LoginManager.session_protection = "strong"

    from desire4memes.queries import get_user

    @LoginManager.user_loader
    def load_user(username: str):
        return get_user(username)


package_dir: Path = Path(__file__).parent.resolve()
project_dir: Path = package_dir.parent.parent.resolve()
      
pep_file: Path = project_dir / "pepper.bin"

with open(pep_file, 'rb') as fin:
    pepper_key = fin.read()

hasher = Hasher(pepper_key = pepper_key)