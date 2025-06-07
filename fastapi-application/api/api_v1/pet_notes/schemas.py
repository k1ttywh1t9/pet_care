from datetime import datetime

from pydantic import BaseModel

from core.types import UserIdType


class PetNoteBase(BaseModel):
    pet_id: int
    content: str


class PetNoteCreate(PetNoteBase):
    pass


class PetNoteRead(PetNoteBase):
    id: int
    user_id: UserIdType
    created_at: datetime


class PetNoteUpdate(PetNoteCreate):
    pet_id: int | None = None
    content: str | None = None
