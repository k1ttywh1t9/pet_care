from fastapi import APIRouter

from api.api_v1.medical_records.schemas import (
    MedicalRecordCreate,
    MedicalRecordRead,
    MedicalRecordUpdate,
)
from core.models import MedicalRecord
from crud import CRUDViewsFactory

router = APIRouter()

crud_router = CRUDViewsFactory(
    model=MedicalRecord,
).get_router(
    create_schema=MedicalRecordCreate,
    read_schema=MedicalRecordRead,
    update_schema=MedicalRecordUpdate,
)

router.include_router(
    router=crud_router,
)
