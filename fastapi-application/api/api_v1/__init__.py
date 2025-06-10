from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from .pets import router as pets_router
from .pet_notes import router as pet_notes_router
from .expense_entry import router as expense_entries_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    router=users_router,
    prefix=settings.api.v1.users,
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
