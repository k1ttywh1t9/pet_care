"""create pet note table

Revision ID: a3f69794f4f8
Revises: 3ac3694046da
Create Date: 2025-06-07 12:31:42.243994

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a3f69794f4f8"
down_revision: Union[str, None] = "3ac3694046da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "pet",
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pet_note",
        sa.Column("pet_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pet_id"],
            ["pet.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.drop_table("pets")


def downgrade() -> None:

    op.create_table(
        "pets",
        sa.Column("name", sa.VARCHAR(length=60), autoincrement=False, nullable=False),
        sa.Column("owner_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"], ["user.id"], name=op.f("pets_owner_id_fkey")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pets_pkey")),
    )

    op.drop_table("pet_note")
    op.drop_table("pet")
