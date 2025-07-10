from typing import Annotated, Optional

from pydantic import Field


class PetIdFieldMixin:
    pet_id: Annotated[int, Field(gt=0)]


class PetIdOptionalFieldMixin:
    pet_id: Annotated[Optional[int], Field(gt=0)] = None
