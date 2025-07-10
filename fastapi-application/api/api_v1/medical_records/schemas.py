from typing import Annotated, Optional

from pydantic import BaseModel, Field

from api.api_v1.mixins import (
    PetIdFieldMixin,
    IdFieldMixin,
    UserIdFieldMixin,
    TimestampMixin,
    PetIdOptionalFieldMixin,
)


class MedicalRecordBase(
    PetIdFieldMixin,
    BaseModel,
):
    name: Annotated[str, Field(max_length=35)]
    file: bytes


class MedicalRecordCreate(
    MedicalRecordBase,
):
    pass


class MedicalRecordRead(
    IdFieldMixin,
    UserIdFieldMixin,
    TimestampMixin,
    MedicalRecordBase,
):
    pass


class MedicalRecordUpdate(
    PetIdOptionalFieldMixin,
    MedicalRecordCreate,
):
    name: Annotated[Optional[str], Field(max_length=35)] = None
    content: bytes | None = None
