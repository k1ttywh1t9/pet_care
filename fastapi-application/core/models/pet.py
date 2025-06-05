from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

from .mixins import IdIntPkMixin
from core.types import UserIdType


class Pet(IdIntPkMixin, Base):
    name: Mapped[str] = mapped_column(String(60))

    owner_id: Mapped[UserIdType] = mapped_column(
        ForeignKey("user.id"),
    )
