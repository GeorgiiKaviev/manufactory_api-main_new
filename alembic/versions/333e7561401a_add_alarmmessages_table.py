"""add AlarmMessages table

Revision ID: 333e7561401a
Revises: 4b56313b5507
Create Date: 2024-06-11 15:15:25.710858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '333e7561401a'
down_revision: Union[str, None] = '4b56313b5507'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alarm_messages',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('tag', sa.Text(), nullable=True),
    sa.Column('camera', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alarm_messages')
    # ### end Alembic commands ###
