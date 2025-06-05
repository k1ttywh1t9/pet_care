from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from mixins.id_int_pk import IdIntPkMixin
from core.types import UserIdType


class Pet(IdIntPkMixin, Base):
    owner: Mapped[UserIdType] = mapped_column(
        ForeignKey("users.id"),
    )
