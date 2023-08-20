from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import Base


class User(Base):
    name = Column(
        String(32),
        nullable=False,
        unique=False,
    )
    username = Column(
        String(50),
        nullable=False,
        unique=True,
    )
    email = Column(
        String(100),
        nullable=True,
        unique=True,
    )

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User: id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r}"

    def __repr__(self):
        return str(self)
