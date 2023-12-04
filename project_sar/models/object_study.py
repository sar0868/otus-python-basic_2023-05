from sqlalchemy.orm import Mapped, relationship

from .base import Base


class ObjectStudy(Base):
    """
    object of study - Объект исследования (раскоп)

    place- место
    year- год
    description (optional)- описание (optional)
    number - номер
    """

    place: Mapped[str]
    year: Mapped[int]
    description: Mapped[str | None]
    number: Mapped[int | None]

    packages = relationship(
        "Package",
        back_populates="object_study",
        uselist=True,
        cascade="save-update, merge, delete",
    )

    def __str__(self):
        return f"Объект, раскоп {self.place}  \
                год {self.year}"

    def __repr__(self):
        return str(self)
