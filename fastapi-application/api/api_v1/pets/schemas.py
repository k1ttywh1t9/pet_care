from typing import Annotated, Optional

from pydantic import BaseModel, Field, HttpUrl

from api.api_v1.mixins import IdFieldMixin, UserIdFieldMixin


class PetBase(BaseModel):
    name: Annotated[str, Field(max_length=35)]
    image_url: Annotated[Optional[HttpUrl], Field()]


class PetRead(IdFieldMixin, UserIdFieldMixin, PetBase):
    pass


class PetCreate(PetBase):
    pass


class PetUpdate(PetCreate):
    name: Annotated[Optional[str], Field(max_length=35)]
    image_url: Annotated[Optional[HttpUrl], Field()]
