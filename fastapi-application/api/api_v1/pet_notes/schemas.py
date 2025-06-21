from pydantic import BaseModel

from api.api_v1.mixins import PetIdMixin, IdMixin, UserIdMixin, TimestampMixin


class PetNoteBase(PetIdMixin, BaseModel):
    content: str


class PetNoteCreate(PetNoteBase):
    pass


class PetNoteRead(IdMixin, UserIdMixin, TimestampMixin, PetNoteBase):
    pass


class PetNoteUpdate(PetNoteCreate):
    pet_id: int | None = None
    content: str | None = None
