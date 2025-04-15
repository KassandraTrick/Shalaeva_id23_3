"""Add initial products

Revision ID: a0f2bb161ebd
Revises: a71fbc102675
Create Date: 2025-04-15 00:58:15.432709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0f2bb161ebd'
down_revision: Union[str, None] = 'a71fbc102675'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
