from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import RelatedToPackageMixin


class ColorAfterFiring(RelatedToPackageMixin, Base):
    """
    color_after_firing - цвет после обжига
    count or 0
    red	    красный
    grey	серый
    white	белый
    """

    red: Mapped[int] = mapped_column(default=0)
    grey: Mapped[int] = mapped_column(default=0)
    white: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return f"Цвет после обжига(id={self.id}, \
                красный={self.red}, \
                серый={self.grey}, \
                белый={self.white})"

    def __repr__(self):
        return str(self)
