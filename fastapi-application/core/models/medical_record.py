from sqlalchemy import Date, Text, LargeBinary
from sqlalchemy.orm import Mapped
from datetime import date

from sqlalchemy.testing.schema import mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin
from core.models.mixins.pet_id_fk import PetIdFkMixin


class MedicalRecord(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    date_performed: Mapped[date] = mapped_column(Date)
    next_due_date: Mapped[date | None] = mapped_column(Date)
    details: Mapped[str] = mapped_column(Text)
    content: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=True,
    )
    is_archived: Mapped[bool]
