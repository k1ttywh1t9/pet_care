from sqlalchemy import Date, Text, LargeBinary, String
from sqlalchemy.orm import Mapped
from datetime import date

from sqlalchemy.testing.schema import mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin
from core.models.mixins.pet_id_fk import PetIdFkMixin


class MedicalRecord(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    name: Mapped[str] = mapped_column(String(60))
    
    content: Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=True,
    )
