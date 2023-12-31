"""create table vesseltypes

Revision ID: 08fcd82162bb
Revises: dda1bff0c5a2
Create Date: 2023-11-30 08:00:12.310311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "08fcd82162bb"
down_revision: Union[str, None] = "dda1bff0c5a2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vesseltypes",
        sa.Column("pot", sa.Integer(), nullable=False),
        sa.Column("lid", sa.Integer(), nullable=False),
        sa.Column("jug", sa.Integer(), nullable=False),
        sa.Column("bowl", sa.Integer(), nullable=False),
        sa.Column("other", sa.Integer(), nullable=False),
        sa.Column("package_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["package_id"],
            ["packages.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vesseltypes")
    # ### end Alembic commands ###
