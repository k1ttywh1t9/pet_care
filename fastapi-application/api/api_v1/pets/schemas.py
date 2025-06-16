from pydantic import BaseModel

from core.types import UserIdType


class PetBase(BaseModel):
    name: str


class PetRead(PetBase):
    id: int
    user_id: UserIdType


class PetCreate(PetBase):
    pass


class PetUpdate(PetCreate):
    name: str | None = None
