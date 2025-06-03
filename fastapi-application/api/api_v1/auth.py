from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from api.api_v1.users_routers_helper import fastapi_users
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(
        backend=authentication_backend,
    )
)
