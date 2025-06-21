from pydantic import BaseModel

from api.api_v1.mixins import UserIdMixin
from api.api_v1.mixins.id import IdMixin, PetIdMixin
from api.api_v1.mixins.timestamp import TimestampMixin


class MedicalRecordBase(PetIdMixin, BaseModel):
    name: str
    content: bytes


class MedicalRecordCreate(MedicalRecordBase):
    pass


class MedicalRecordRead(IdMixin, UserIdMixin, TimestampMixin, MedicalRecordBase):
    pass


class MedicalRecordUpdate(MedicalRecordCreate):
    pet_id: int | None = None
    name: str | None = None
    content: str | None = None
