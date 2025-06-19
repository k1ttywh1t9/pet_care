"""update foreign keys + medical record table

Revision ID: b53c8f10a78e
Revises: b46454b58e50
Create Date: 2025-06-19 14:59:20.580586

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b53c8f10a78e"
down_revision: Union[str, None] = "b46454b58e50"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        op.f("expense_entry_pet_id_fkey"), "expense_entry", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("expense_entry_user_id_fkey"), "expense_entry", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_expense_entry_user_id_user"),
        "expense_entry",
        "user",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        op.f("fk_expense_entry_pet_id_pet"),
        "expense_entry",
        "pet",
        ["pet_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.add_column(
        "medical_record",
        sa.Column("name", sa.String(length=60), nullable=False),
    )
    op.drop_constraint(
        op.f("medical_record_user_id_fkey"),
        "medical_record",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("medical_record_pet_id_fkey"),
        "medical_record",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_medical_record_pet_id_pet"),
        "medical_record",
        "pet",
        ["pet_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        op.f("fk_medical_record_user_id_user"),
        "medical_record",
        "user",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_column("medical_record", "details")
    op.drop_column("medical_record", "next_due_date")
    op.drop_column("medical_record", "date_performed")
    op.drop_column("medical_record", "is_archived")
    op.drop_constraint(op.f("pet_user_id_fkey"), "pet", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_pet_user_id_user"),
        "pet",
        "user",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_constraint(
        op.f("pet_note_pet_id_fkey"), "pet_note", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("pet_note_user_id_fkey"), "pet_note", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_pet_note_user_id_user"),
        "pet_note",
        "user",
        ["user_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_foreign_key(
        op.f("fk_pet_note_pet_id_pet"),
        "pet_note",
        "pet",
        ["pet_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_pet_note_pet_id_pet"), "pet_note", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_pet_note_user_id_user"), "pet_note", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("pet_note_user_id_fkey"), "pet_note", "user", ["user_id"], ["id"]
    )
    op.create_foreign_key(
        op.f("pet_note_pet_id_fkey"), "pet_note", "pet", ["pet_id"], ["id"]
    )
    op.drop_constraint(op.f("fk_pet_user_id_user"), "pet", type_="foreignkey")
    op.create_foreign_key(
        op.f("pet_user_id_fkey"), "pet", "user", ["user_id"], ["id"]
    )
    op.add_column(
        "medical_record",
        sa.Column(
            "is_archived", sa.BOOLEAN(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "medical_record",
        sa.Column(
            "date_performed", sa.DATE(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "medical_record",
        sa.Column(
            "next_due_date", sa.DATE(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "medical_record",
        sa.Column("details", sa.TEXT(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(
        op.f("fk_medical_record_user_id_user"),
        "medical_record",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_medical_record_pet_id_pet"),
        "medical_record",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("medical_record_pet_id_fkey"),
        "medical_record",
        "pet",
        ["pet_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("medical_record_user_id_fkey"),
        "medical_record",
        "user",
        ["user_id"],
        ["id"],
    )
    op.drop_column("medical_record", "name")
    op.drop_constraint(
        op.f("fk_expense_entry_pet_id_pet"),
        "expense_entry",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_expense_entry_user_id_user"),
        "expense_entry",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("expense_entry_user_id_fkey"),
        "expense_entry",
        "user",
        ["user_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("expense_entry_pet_id_fkey"),
        "expense_entry",
        "pet",
        ["pet_id"],
        ["id"],
    )
