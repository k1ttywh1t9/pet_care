from pydantic import BaseModel

from pydantic import BaseModel

from api.api_v1.mixins.id import IdMixin, PetIdMixin
from api.api_v1.mixins.timestamp import TimestampMixin


class MedicalRecordBase(BaseModel):
    name: str
    content: bytes


class MedicalRecordCreate(MedicalRecordBase):
    pass


class MedicalRecordRead(IdMixin, PetIdMixin, TimestampMixin, MedicalRecordBase):
    pass


class MedicalRecordUpdate(MedicalRecordCreate):
    name: str | None = None
    content: str | None = None
