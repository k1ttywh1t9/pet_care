from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin, PetIdFkMixin

if TYPE_CHECKING:
    from .pet import Pet


class ExpenseEntry(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    amount: Mapped[int]
    purpose: Mapped[str | None]

    pet: Mapped["Pet"] = relationship(
        back_populates="expense_entries",
    )
    load_relations: list[str] = ["pet"]
