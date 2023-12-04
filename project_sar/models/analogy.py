from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship, mapped_column

from .packages_analogies_association import packages_analogies_association
from .base import Base

if TYPE_CHECKING:
    from . import Package


class Analogy(Base):
    """
    analogies - аналогии

        source          источник
        link            ссылка
        description     описание
    """

    __tablename__ = "analogies"
    source: Mapped[str]
    link: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]

    packages: Mapped[list["Package"]] = relationship(
        secondary=packages_analogies_association,
        back_populates="analogies",
    )

    def __str__(self):
        return f"Аналогия: \
                источник - {self.source} \
                ссылка - {self.link} \
                описание - {self.description}"

    def __repr__(self):
        return str(self)
