"""Add initial products

Revision ID: a71fbc102675
Revises: d0d51eb608ad
Create Date: 2025-04-15 00:57:09.215647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a71fbc102675'
down_revision: Union[str, None] = 'd0d51eb608ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
