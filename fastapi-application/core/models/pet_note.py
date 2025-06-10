from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin


class PetNote(IdIntPkMixin, UserIdFkMixin, TimestampMixin, Base):
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id"))

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
