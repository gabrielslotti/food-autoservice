"""create main tables

Revision ID: 4fba9f51e61b
Revises:
Create Date: 2024-08-12 19:37:22.172068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '4fba9f51e61b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create customer table
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('cpf', sa.String(length=11), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('first_name', sa.String(length=60), nullable=False),
        sa.Column('last_name', sa.String(length=60), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_customer')),
        sa.UniqueConstraint('cpf', name=op.f('uq_customer_cpf'))
    )

    # Create items_category table
    op.create_table(
        'items_category',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('description', sa.String(40), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_items_category'))
    )

    # Create items table
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('title', sa.String(length=120), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('category', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Integer(), nullable=False),
        sa.Column('price', sa.Numeric(precision=16, scale=4), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_items')),
        sa.ForeignKeyConstraint(('category',), ['items_category.id'], name=op.f('fk_items_category'))  # noqa
    )

    # Create order_status table
    op.create_table(
        'order_status',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('description', sa.String(20), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_order_status'))
    )

    # Create order table
    op.create_table(
        'order',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('status', sa.Integer(), nullable=False),
        sa.Column('items', JSONB(astext_type=sa.Text()), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_order')),
        sa.ForeignKeyConstraint(('status',), ['order_status.id'], name=op.f('fk_order_status'))  # noqa
    )

    # Insert values on items_category table
    meta = sa.MetaData()
    items_category = sa.Table('items_category', meta, autoload_with=op.get_bind())  # noqa

    op.bulk_insert(
        items_category,
        [
            {'description': 'Lanche'},
            {'description': 'Acompanhamento'},
            {'description': 'Bebida'},
            {'description': 'Sobremesa'}
        ]
    )

    # Insert values on order_status table
    meta = sa.MetaData()
    order_status = sa.Table('order_status', meta, autoload_with=op.get_bind())

    op.bulk_insert(
        order_status,
        [
            {'description': 'Recebido'},
            {'description': 'Em preparação'},
            {'description': 'Pronto'},
            {'description': 'Finalizado'}
        ]
    )


def downgrade() -> None:
    pass
