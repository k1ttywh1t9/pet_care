from datetime import date

from pydantic import BaseModel

from api.api_v1.mixins.id import IdMixin, UserIdMixin, PetIdMixin
from api.api_v1.mixins.timestamp import TimestampMixin


class MedicalRecordBase(BaseModel):
    date_performed: date
    next_due_date: date
    details: str
    content: bytes
    is_archived: bool


class MedicalRecordCreate(MedicalRecordBase):
    pass


class MedicalRecordRead(IdMixin, PetIdMixin, TimestampMixin, MedicalRecordBase):
    pass


class MedicalRecordUpdate(MedicalRecordCreate):
    date_performed: date | None = None
    next_due_date: date | None = None
    details: str | None = None
    content: bytes | None = None
    is_archived: bool | None = None
