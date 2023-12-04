from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .packages_analogies_association import packages_analogies_association
from .base import Base

if TYPE_CHECKING:
    from . import Analogy
    from . import ObjectStudy
    from . import VesselType
    from . import PartPot
    from . import ColorAfterFiring


class Package(Base):
    number: Mapped[int]
    passport: Mapped[str]
    layer_number: Mapped[int] = mapped_column(default=0)
    mainland_hole: Mapped[str] = mapped_column(default="")
    object_study_id: Mapped[int] = mapped_column(ForeignKey("objectstudys.id"))
    object_study: Mapped["ObjectStudy"] = relationship(back_populates="packages")
    vessel_types: Mapped["VesselType"] = relationship(
        back_populates="package",
        cascade="all, delete-orphan",
    )
    part_of_the_pots: Mapped["PartPot"] = relationship(
        back_populates="package",
        cascade="all, delete-orphan",
    )
    color_after_firing: Mapped["ColorAfterFiring"] = relationship(
        back_populates="package",
        cascade="all, delete-orphan",
    )

    analogies: Mapped[list["Analogy"]] = relationship(
        secondary=packages_analogies_association,
        back_populates="packages",
    )

    def __str__(self):
        return f"Пакет N{self.number} \
                слой {self.layer_number} \
                м.яма {self.mainland_hole}"

    def __repr__(self):
        return str(self)
