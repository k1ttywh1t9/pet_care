from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin, PetIdFkMixin

if TYPE_CHECKING:
    from .pet import Pet


class PetNote(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    pet: Mapped["Pet"] = relationship()
