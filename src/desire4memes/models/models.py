from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from desire4memes.extensions import db

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    username: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(64))

class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    title: Mapped[str] = mapped_column(String(64))
    image: Mapped[bytes] = mapped_column(LargeBinary)
    toptext: Mapped[str] = mapped_column(String(64))
    bottomtext: Mapped[str] = mapped_column(String(64))
    caption: Mapped[str] = mapped_column(String(128))
    user: Mapped[User] = relationship(viewonly = True, lazy = "dynamic")