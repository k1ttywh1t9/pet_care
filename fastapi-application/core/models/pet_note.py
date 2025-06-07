from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin
from core.types import UserIdType


class PetNote(IdIntPkMixin, Base):
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id"))
    user_id: Mapped[UserIdType] = mapped_column(ForeignKey("user.id"))
