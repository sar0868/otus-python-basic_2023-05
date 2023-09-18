from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import db
from .users import User


class Post(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=False)
    body: Mapped[str | None] = mapped_column(
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )

    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    def __str__(self):
        return f"Post: id={self.id}, title={self.title!r}, body={self.body!r}"

    def __repr__(self):
        return str(self)
