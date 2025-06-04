from fastapi import APIRouter

from api.api_v1.schemas.user import UserRead, UserCreate
from api.dependencies.authentication.backend import authentication_backend
from api.api_v1.fastapi_users_routers_helper import fastapi_users
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)


# login
# logout
router.include_router(
    router=fastapi_users.get_auth_router(
        backend=authentication_backend,
    )
)


# register
router.include_router(
    router=fastapi_users.get_register_router(
        user_schema=UserRead,
        user_create_schema=UserCreate,
    )
)
