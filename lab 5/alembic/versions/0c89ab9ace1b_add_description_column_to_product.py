"""Add description column to product

Revision ID: 0c89ab9ace1b
Revises: 6c00a8a7ffc4
Create Date: 2025-04-15 00:53:51.965360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from app.models.product import Product

# revision identifiers, used by Alembic.
revision: str = '0c89ab9ace1b'
down_revision: Union[str, None] = '6c00a8a7ffc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    bind = op.get_bind()
    session = sessionmaker(bind=bind)()
    session.add_all([
        Product(name="Apple", description="Fresh red apple", price=1.2),
        Product(name="Banana", description="Yellow ripe banana", price=0.5),
        Product(name="Orange", description="Juicy orange", price=0.8),
        Product(name="Strawberry", description="Sweet red strawberry", price=2.5),
        Product(name="Pineapple", description="Tropical pineapple", price=3.0),
    ])
    session.commit()


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('discription', sa.TEXT(), nullable=True),
    sa.Column('price', sa.REAL(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
