"""create_table_of_regestration

Revision ID: 74d0347410b9
Revises: 299fef7848ab
Create Date: 2024-03-21 21:15:23.812905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74d0347410b9'
down_revision: Union[str, None] = '299fef7848ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requisites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bank', sa.String(length=100), nullable=False),
    sa.Column('bik', sa.Integer(), nullable=False),
    sa.Column('rs', sa.Integer(), nullable=False),
    sa.Column('ks', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bik'),
    sa.UniqueConstraint('ks'),
    sa.UniqueConstraint('rs')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requisites')
    # ### end Alembic commands ###