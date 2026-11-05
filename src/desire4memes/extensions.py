from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from desire4memes.authentication import Hasher

db = SQLAlchemy()
lm = LoginManager()
hasher = Hasher()