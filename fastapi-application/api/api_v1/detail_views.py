from fastapi import APIRouter

from api.api_v1.detail_schemas import (
    PetDetailsRead,
    PetNoteDetailsRead,
    ExpenseEntryDetailsRead,
    MedicalRecordDetailsRead,
)
from core.config import settings
from core.models import Pet, PetNote, ExpenseEntry, MedicalRecord
from crud.elements.read_service import ReadService
from crud_router.elements.read_router import ReadRouterFactory

router = APIRouter(
    tags=["Detail"],
)

read_pet_details_router = ReadRouterFactory(
    model=Pet,
    service=ReadService(
        model=Pet,
    ),
).get_router(
    read_schema=PetDetailsRead,
)

read_pet_note_details_router = ReadRouterFactory(
    model=PetNote,
    service=ReadService(
        model=PetNote,
    ),
).get_router(
    read_schema=PetNoteDetailsRead,
)

read_expense_entry_details_router = ReadRouterFactory(
    model=ExpenseEntry,
    service=ReadService(
        model=ExpenseEntry,
    ),
).get_router(
    read_schema=ExpenseEntryDetailsRead,
)

read_medical_record_details_router = ReadRouterFactory(
    model=MedicalRecord,
    service=ReadService(
        model=MedicalRecord,
    ),
).get_router(
    read_schema=MedicalRecordDetailsRead,
)

router.include_router(
    router=read_pet_details_router,
    prefix=settings.api.v1.pets + "/detail",
)

router.include_router(
    router=read_pet_note_details_router,
    prefix=settings.api.v1.pet_notes + "/detail",
)

router.include_router(
    router=read_expense_entry_details_router,
    prefix=settings.api.v1.expense_entries + "/detail",
)

router.include_router(
    router=read_medical_record_details_router,
    prefix=settings.api.v1.medical_records + "/detail",
)
