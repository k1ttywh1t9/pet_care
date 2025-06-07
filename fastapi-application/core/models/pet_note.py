from datetime import datetime

from sqlalchemy import ForeignKey, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin
from core.types import UserIdType


class PetNote(IdIntPkMixin, Base):
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id"))
    user_id: Mapped[UserIdType] = mapped_column(ForeignKey("user.id"))

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
