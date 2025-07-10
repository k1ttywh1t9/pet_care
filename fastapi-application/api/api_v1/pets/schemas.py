from typing import Annotated, Optional

from pydantic import BaseModel, Field, HttpUrl

from api.api_v1.mixins import IdFieldMixin, UserIdFieldMixin


class PetBase(BaseModel):
    name: Annotated[str, Field(max_length=35)]


class PetRead(IdFieldMixin, UserIdFieldMixin, PetBase):
    image_url: str | None = None


class PetCreate(PetBase):
    pass


class PetUpdate(PetCreate):
    name: Annotated[Optional[str], Field(max_length=35)] = None


class PetAvatarUpdate(PetUpdate):
    image_url: HttpUrl
