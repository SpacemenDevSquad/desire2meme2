from typing import Any, Dict

from sqlalchemy import String, Integer, LargeBinary, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from desire4memes.extensions import db

class Meme(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(64))
    image: Mapped[bytes] = mapped_column(LargeBinary)
    fabric: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable = True)
    caption: Mapped[str] = mapped_column(String(128))

class User(db.Model):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(64), primary_key = True)
    password: Mapped[bytes] = mapped_column(LargeBinary)
    memes: Mapped[list[Meme]] = relationship(lazy = "dynamic")