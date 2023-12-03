from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint, Integer

from models import Base

packages_analogies_association = Table(
    "packages_analogies_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("package_id", ForeignKey("packages.id"), nullable=False),
    Column("analogy_id", ForeignKey("analogies.id"), nullable=False),
    UniqueConstraint("package_id", "analogy_id", name="index_unique_package_analogy"),
)
