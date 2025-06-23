from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdIntPkMixin, UserIdFkMixin

if TYPE_CHECKING:
    from .user import User
    from .pet_note import PetNote
    from .expense_entry import ExpenseEntry
    from .medical_record import MedicalRecord


class Pet(IdIntPkMixin, UserIdFkMixin, Base):
    name: Mapped[str] = mapped_column(String(60))

    owner: Mapped["User"] = relationship(back_populates="pets")
    notes: Mapped[list["PetNote"]] = relationship(
        back_populates="pet",
    )
    expense_entries: Mapped[list["ExpenseEntry"]] = relationship(
        back_populates="pet",
    )
    medical_records: Mapped[list["MedicalRecord"]] = relationship(
        back_populates="pet",
    )
    load_relations: list[str] = ["notes", "expense_entries", "medical_records"]
