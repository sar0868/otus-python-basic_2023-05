from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import RelatedToPackageMixin


class PartPot(RelatedToPackageMixin, Base):
    """
    part_of_the_pot - часть горшка
    count or 0
    whisk   венчик
    wall    стенка
    bottom  дно
    """

    whisk: Mapped[int] = mapped_column(default=0)
    wall: Mapped[int] = mapped_column(default=0)
    bottom: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return f"Часть горшка (id={self.id}, \
        венчики={self.whisk}, стенки={self.wall},\
        дно={self.bottom})"

    def __repr__(self):
        return str(self)
