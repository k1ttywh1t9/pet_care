"""add image_url field to pet model

Revision ID: 3a38ccc0fe25
Revises: b53c8f10a78e
Create Date: 2025-07-05 16:06:29.571039

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3a38ccc0fe25"
down_revision: Union[str, None] = "b53c8f10a78e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("pet", sa.Column("image_url", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("pet", "image_url")
