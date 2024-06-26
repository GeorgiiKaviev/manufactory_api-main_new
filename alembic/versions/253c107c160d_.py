"""empty message

Revision ID: 253c107c160d
Revises: 
Create Date: 2024-05-07 12:35:57.979166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '253c107c160d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations_history',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('place_id', sa.Text(), nullable=True),
    sa.Column('program', sa.Text(), nullable=True),
    sa.Column('data', sa.Text(), nullable=True),
    sa.Column('dt_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations_history')
    # ### end Alembic commands ###
