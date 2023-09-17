from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import db
from .posts import Post


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    email: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True,
    )

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"User: id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r}"

    def __repr__(self):
        return str(self)
