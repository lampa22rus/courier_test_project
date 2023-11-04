"""empty message

Revision ID: 14b316e5d4fb
Revises: 
Create Date: 2023-11-04 17:16:28.306640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14b316e5d4fb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('districts', sa.ARRAY(sa.String(length=20)), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_couriers_districts'), 'couriers', ['districts'], unique=False)
    op.create_index(op.f('ix_couriers_id'), 'couriers', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('districts', sa.String(length=20), nullable=True),
    sa.Column('status', sa.Enum('works', 'complited', name='status'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('completed_order', sa.DateTime(), nullable=True),
    sa.Column('courier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_completed_order'), 'orders', ['completed_order'], unique=False)
    op.create_index(op.f('ix_orders_courier_id'), 'orders', ['courier_id'], unique=False)
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_courier_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_completed_order'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_couriers_id'), table_name='couriers')
    op.drop_index(op.f('ix_couriers_districts'), table_name='couriers')
    op.drop_table('couriers')
    # ### end Alembic commands ###
