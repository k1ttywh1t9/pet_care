from typing import Annotated, Optional

from pydantic import BaseModel, Field

from api.api_v1.mixins import IdFieldMixin, UserIdFieldMixin


class PetBase(BaseModel):
    name: Annotated[str, Field(max_length=35)]
    image_url: str | None = None


class PetRead(IdFieldMixin, UserIdFieldMixin, PetBase):
    pass


class PetCreate(PetBase):
    pass


class PetUpdate(PetCreate):
    name: Annotated[Optional[str], Field(max_length=35)]
