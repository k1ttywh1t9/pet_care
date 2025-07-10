from typing import Annotated, Optional

from pydantic import BaseModel, Field, ConfigDict

from api.api_v1.mixins import (
    TimestampMixin,
    PetIdFieldMixin,
    PetIdOptionalFieldMixin,
    IdFieldMixin,
    UserIdFieldMixin,
)


class ExpenseEntryBase(
    PetIdFieldMixin,
    BaseModel,
):
    amount: Annotated[int, Field(ge=0)]
    purpose: Annotated[str, Field(max_length=35)]


class ExpenseEntryCreate(
    ExpenseEntryBase,
):
    pass


class ExpenseEntryRead(
    IdFieldMixin,
    UserIdFieldMixin,
    TimestampMixin,
    ExpenseEntryBase,
):
    model_config = ConfigDict(from_attributes=True)


class ExpenseEntryUpdate(
    PetIdOptionalFieldMixin,
    ExpenseEntryCreate,
):
    amount: Annotated[Optional[int], Field(ge=0)] = None
    purpose: Annotated[Optional[str], Field(max_length=35)] = None
