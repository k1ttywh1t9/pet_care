from typing import Annotated, Optional

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    HttpUrl,
    field_validator,
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
    document_url: str


class MedicalRecordUpdate(
    PetIdOptionalFieldMixin,
    MedicalRecordCreate,
):
    name: Annotated[Optional[str], Field(max_length=35)] = None


class MedicalRecordDocumentUpdate(
    MedicalRecordUpdate,
):
    document_url: str

    @field_validator("document_url", mode="after")
    @classmethod
    def validate_document_url(cls, url: str) -> str:
        if url is None:
            return None
        return url
