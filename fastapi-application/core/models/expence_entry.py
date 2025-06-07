from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin
from core.types import UserIdType


class ExpenseEntry(IdIntPkMixin, Base):
    pet_id: Mapped[UserIdType] = mapped_column(ForeignKey("pet.id"))
    amount: Mapped[int] = mapped_column()
    purpose: Mapped[str | None] = mapped_column()
