from datetime import datetime
from mixin import RelatedToUserMixin

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime, func, ForeignKey
)
from sqlalchemy.orm import relationship

from models import Base


class Post(RelatedToUserMixin, Base):
    title = Column(String(60), nullable=False, unique=False)
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    def __str__(self):
        return f"Post: id={self.id}, title={self.title!r}, body={self.body!r}"

    def __repr__(self):
        return str(self)
