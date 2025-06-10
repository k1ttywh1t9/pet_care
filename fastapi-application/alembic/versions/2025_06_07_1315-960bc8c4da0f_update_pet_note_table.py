"""update pet note table

Revision ID: 960bc8c4da0f
Revises: af2057ea2461
Create Date: 2025-06-07 13:15:37.881504

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "960bc8c4da0f"
down_revision: Union[str, None] = "af2057ea2461"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "pet_note",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("pet_note", "created_at")
