from typing import Annotated, Optional

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    HttpUrl,
)

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
    document_url: str | None = None

    model_config = ConfigDict(from_attributes=True)


class MedicalRecordUpdate(
    PetIdOptionalFieldMixin,
    MedicalRecordCreate,
):
    name: Annotated[Optional[str], Field(max_length=35)] = None


class MedicalRecordDocumentUpdate(
    MedicalRecordUpdate,
):
    document_url: str
