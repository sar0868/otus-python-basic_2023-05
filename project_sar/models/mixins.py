from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, mapped_column, relationship


class RelatedToPackageMixin:
    _package_back_populates = ""

    @declared_attr
    def package_id(cls):
        return mapped_column(ForeignKey("packages.id"))

    @declared_attr
    def package(cls):
        return relationship(
            "Package",
            back_populates=cls._package_back_populates,
        )
