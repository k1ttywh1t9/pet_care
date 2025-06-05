from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

from .mixins import IdIntPkMixin
from core.types import UserIdType


if TYPE_CHECKING:
    from .user import User


class Pet(IdIntPkMixin, Base):
    name: Mapped[str] = mapped_column(String(60))

    owner_id: Mapped[UserIdType] = mapped_column(
        ForeignKey("user.id"),
    )

    owner: Mapped["User"] = relationship(back_populates="pets")
