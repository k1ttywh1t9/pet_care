from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin
from core.models.mixins.pet_id_fk import PetIdFkMixin


class PetNote(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
