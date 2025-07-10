"""add document url field to MR instead of byte content

Revision ID: d88ebc5bc200
Revises: 3a38ccc0fe25
Create Date: 2025-07-10 14:00:11.973208

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "d88ebc5bc200"
down_revision: Union[str, None] = "3a38ccc0fe25"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "medical_record", sa.Column("document_url", sa.String(), nullable=True)
    )
    op.drop_column("medical_record", "content")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "medical_record",
        sa.Column("content", postgresql.BYTEA(), autoincrement=False, nullable=True),
    )
    op.drop_column("medical_record", "document_url")
