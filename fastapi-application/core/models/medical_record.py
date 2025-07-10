from typing import TYPE_CHECKING

from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from core.models.mixins import IdIntPkMixin, TimestampMixin, UserIdFkMixin, PetIdFkMixin

if TYPE_CHECKING:
    from .pet import Pet


class MedicalRecord(IdIntPkMixin, UserIdFkMixin, PetIdFkMixin, TimestampMixin, Base):
    name: Mapped[str] = mapped_column(String(60))
    document_url: Mapped[str | None]

    pet: Mapped["Pet"] = relationship(
        back_populates="medical_records",
    )
    load_relations: list[str] = ["pet"]
