from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import db
# from .posts import Post


class User(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    email: Mapped[str | None]

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return f"User: id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r}"

    def __repr__(self):
        return str(self)


# class Post(db.Model):
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(nullable=False, unique=False)
#     body: Mapped[str | None] = mapped_column(
#         nullable=False,
#         unique=False,
#         default="",
#         server_default="",
#     )
#     user_id: Mapped[int] = mapped_column(
#         db.ForeignKey("user.id"),
#     )
#
#     user: Mapped["User"] = relationship(
#         back_populates="posts",
#     )
#
#     def __str__(self):
#         return f"Post: id={self.id}, title={self.title!r}, body={self.body!r}"
#
#     def __repr__(self):
#         return str(self)

