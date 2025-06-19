from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdIntPkMixin, UserIdFkMixin

if TYPE_CHECKING:
    from .user import User


class Pet(IdIntPkMixin, UserIdFkMixin, Base):
    name: Mapped[str] = mapped_column(String(60))

    owner: Mapped["User"] = relationship(back_populates="pets")
