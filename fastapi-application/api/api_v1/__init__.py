from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from api.api_v1.detail.views import router as detail_router
from .pets import router as pets_router
from .pet_notes import router as pet_notes_router
from .expense_entries import router as expense_entries_router
from .medical_records import router as medical_records_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    router=users_router,
    prefix=settings.api.v1.users,
)


router.include_router(
    router=detail_router,
)

router.include_router(
    router=pets_router,
    prefix=settings.api.v1.pets,
)

router.include_router(
    router=pet_notes_router,
    prefix=settings.api.v1.pet_notes,
)

router.include_router(
    router=expense_entries_router,
    prefix=settings.api.v1.expense_entries,
)

router.include_router(
    router=medical_records_router,
    prefix=settings.api.v1.medical_records,
)
