"""create pet table

Revision ID: 1a4e20ff31c0
Revises: eace13a2d248
Create Date: 2025-06-05 07:35:45.499344

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1a4e20ff31c0"
down_revision: Union[str, None] = "eace13a2d248"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pets",
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("owner", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("Pets")
