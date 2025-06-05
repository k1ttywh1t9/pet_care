from fastapi import APIRouter

from core.config import settings
from api.api_v1.users.auth import router as auth_router
from api.api_v1.users.views import router as users_router
from api.api_v1.pets.views import router as pets_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    auth_router,
)

router.include_router(
    pets_router,
)

router.include_router(
    users_router,
)
