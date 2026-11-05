from sqlalchemy import asc, desc, Select

from desire4memes.extensions import db
from desire4memes.models import User, Meme

def get_user(username: str) -> User | None:
    query: Select[User] = db.select(User).where(User.username == username)
    return db.session.scalar(query)

def get_user_memes(id: int) -> list[Meme]:
    query: Select[User] = db.select(User.memes).where(User.id == id).order_by(desc(User.memes.id)).limit(10)
    return db.session.scalars(query).all()