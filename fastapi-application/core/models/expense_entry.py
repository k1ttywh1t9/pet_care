from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin
from core.models.mixins.pet_id_fk import PetIdFkMixin


class ExpenseEntry(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    amount: Mapped[int] = mapped_column()
    purpose: Mapped[str | None] = mapped_column()
