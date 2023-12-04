"""create table colorafterfirings

Revision ID: 6c170d0fb7d3
Revises: 80acda186b69
Create Date: 2023-11-30 08:03:04.435074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6c170d0fb7d3"
down_revision: Union[str, None] = "80acda186b69"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "colorafterfirings",
        sa.Column("red", sa.Integer(), nullable=False),
        sa.Column("grey", sa.Integer(), nullable=False),
        sa.Column("white", sa.Integer(), nullable=False),
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
    op.drop_table("colorafterfirings")
    # ### end Alembic commands ###