from pydantic import BaseModel

from core.types import UserIdType


class PetBase(BaseModel):
    name: str
    owner_id: UserIdType


class PetRead(PetBase):
    id: int


class PetCreate(PetBase):
    pass


class PetUpdate(PetBase):
    pass
