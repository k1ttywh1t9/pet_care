from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin


class ExpenseEntry(IdIntPkMixin, UserIdFkMixin, TimestampMixin, Base):
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id"))
    amount: Mapped[int] = mapped_column()
    purpose: Mapped[str | None] = mapped_column()
