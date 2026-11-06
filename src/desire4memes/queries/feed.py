from sqlalchemy import asc, desc, Select

from desire4memes.extensions import db
from desire4memes.models import Meme

def get_recent_memes() -> list[Meme]:
    query: Select[tuple[Meme]] = db.select(Meme).order_by(desc(Meme.id)).limit(10)
    return db.session.scalars(query).all()

def get_recent_memes_with_start(starting_id: int) -> list[Meme]:
    query: Select[tuple[Meme]] = db.select(Meme).where(Meme.id < starting_id).order_by(desc(Meme.id)).limit(10)
    return db.session.scalars(query).all()

def get_oldest_memes() -> list[Meme]:
    query: Select[tuple[Meme]] = db.select(Meme).order_by(asc(Meme.id)).limit(10)
    return db.session.scalars(query).all()

def get_oldest_memes_with_start(starting_id: int) -> list[Meme]:
    query: Select[tuple[Meme]] = db.select(Meme).where(Meme.id > starting_id).order_by(desc(Meme.id)).limit(10)
    return db.session.scalars(query).all()