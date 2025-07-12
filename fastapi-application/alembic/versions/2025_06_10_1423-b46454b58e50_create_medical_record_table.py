"""create medical_record table

Revision ID: b46454b58e50
Revises: 9a73c0970694
Create Date: 2025-06-10 14:23:48.760842

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b46454b58e50"
down_revision: Union[str, None] = "9a73c0970694"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "medical_record",
        sa.Column("date_performed", sa.Date(), nullable=False),
        sa.Column("next_due_date", sa.Date(), nullable=True),
        sa.Column("details", sa.Text(), nullable=False),
        sa.Column("content", sa.LargeBinary(), nullable=True),
        sa.Column("is_archived", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("pet_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["pet_id"],
            ["pet.id"],
            "medical_record_pet_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            "medical_record_user_id_fkey",
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("medical_record")
