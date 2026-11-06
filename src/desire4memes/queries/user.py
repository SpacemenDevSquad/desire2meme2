from sqlalchemy import asc, desc, Select

from desire4memes.extensions import db
from desire4memes.models import User, Meme

def get_user(username: str) -> User | None:
    query: Select[tuple[User]] = db.select(User).where(User.username == username)
    return db.session.scalar(query)

def get_user_memes(username: str) -> list[Meme]:
    query: Select[tuple[User]] = db.select(User.memes).where(User.username == username).order_by(desc(User.memes.id)).limit(10)
    return db.session.scalars(query).all()