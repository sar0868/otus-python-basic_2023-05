"""alter table post: title varchar 120

Revision ID: 2500ba49f2b3
Revises: a4189b71d800
Create Date: 2023-08-22 22:49:58.469826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2500ba49f2b3'
down_revision: Union[str, None] = 'a4189b71d800'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=120),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'title',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###