from typing import Annotated, Optional

from pydantic import BaseModel, Field

from api.api_v1.mixins import TimestampMixin, IdFieldMixin, UserIdFieldMixin
from api.api_v1.mixins.pet_id_mixin import PetIdOptionalFieldMixin, PetIdFieldMixin


class PetNoteBase(PetIdFieldMixin, BaseModel):
    content: Annotated[str, Field(max_length=255)]


class PetNoteCreate(PetNoteBase):
    pass


class PetNoteRead(IdFieldMixin, UserIdFieldMixin, TimestampMixin, PetNoteBase):
    pass


class PetNoteUpdate(PetIdOptionalFieldMixin, PetNoteCreate):
    content: Annotated[Optional[str], Field(max_length=255)]
