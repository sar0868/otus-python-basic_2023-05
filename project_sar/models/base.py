from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    Mapped,
    mapped_column,
)


class Base:
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


Base = declarative_base(cls=Base)
