from pydantic import BaseModel

from api.api_v1.mixins import IdMixin, UserIdMixin


class PetBase(BaseModel):
    name: str


class PetRead(IdMixin, UserIdMixin, PetBase):
    pass


class PetCreate(PetBase):
    pass


class PetUpdate(PetCreate):
    name: str | None = None
