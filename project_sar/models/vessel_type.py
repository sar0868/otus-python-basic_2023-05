from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import RelatedToPackageMixin


class VesselType(RelatedToPackageMixin, Base):
    """
    vessel_type - тип сосуда
    count or 0
    pot     горшок
    lid     крышка
    jug     кувшин
    Bowl    миска
    other   другое
    """

    pot: Mapped[int] = mapped_column(default=0)
    lid: Mapped[int] = mapped_column(default=0)
    jug: Mapped[int] = mapped_column(default=0)
    bowl: Mapped[int] = mapped_column(default=0)
    other: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return f"Тип сосуда(id={self.id}, \
        горшок={self.pot}, \
        крышка={self.lid}, \
        кувшин={self.jug}, \
        миска={self.bowl} \
        другое={self.other})"

    def __repr__(self):
        return str(self)
