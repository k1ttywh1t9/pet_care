"""update pet note table

Revision ID: af2057ea2461
Revises: a3f69794f4f8
Create Date: 2025-06-07 13:07:40.020892

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "af2057ea2461"
down_revision: Union[str, None] = "a3f69794f4f8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("pet_note", sa.Column("content", sa.Text(), nullable=False))


def downgrade() -> None:
    op.drop_column("pet_note", "content")
