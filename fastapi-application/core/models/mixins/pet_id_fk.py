from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class PetIdFkMixin:
    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id", ondelete="SET NULL"))
