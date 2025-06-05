from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from core.config import settings
from core.models import User
from core.types import UserIdType
from .schemas import UserRead, UserUpdate
from api.dependencies.authentication.backend import authentication_backend
from api.dependencies.authentication.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
