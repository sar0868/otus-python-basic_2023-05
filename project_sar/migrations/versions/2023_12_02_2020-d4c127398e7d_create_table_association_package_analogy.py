"""create table association package analogy

Revision ID: d4c127398e7d
Revises: b467d71c8e64
Create Date: 2023-12-02 20:20:55.868919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d4c127398e7d"
down_revision: Union[str, None] = "b467d71c8e64"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "packages_analogies_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("package_id", sa.Integer(), nullable=False),
        sa.Column("analogy_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["analogy_id"],
            ["analogies.id"],
        ),
        sa.ForeignKeyConstraint(
            ["package_id"],
            ["packages.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "package_id", "analogy_id", name="index_unique_package_analogy"
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("packages_analogies_association")
    # ### end Alembic commands ###
