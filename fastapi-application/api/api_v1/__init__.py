from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from .pets import router as pets_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    router=users_router,
)

router.include_router(
    router=pets_router,
)
