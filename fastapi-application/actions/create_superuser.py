import asyncio
import contextlib

import logging

from api.api_v1.users.schemas import UserCreate

log = logging.getLogger(__name__)

from fastapi_users.exceptions import UserAlreadyExists


from api.dependencies.authentication.user_manager import get_user_manager
from api.dependencies.authentication.users import get_users_db
from core.authentication import UserManager
from core.config import settings
from core.models import User, db_helper

get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str,
    password: str,
    is_active: bool,
    is_superuser: bool,
    is_verified: bool,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    try:
        async with db_helper.session_factory() as session:
            async with get_users_db_context(session) as users_db:
                async with get_user_manager_context(users_db) as user_manager:
                    return await create_user(
                        user_manager=user_manager, user_create=user_create
                    )
    except UserAlreadyExists:
        log.warning("User %r already exists", email)


if __name__ == "__main__":
    asyncio.run(create_superuser(**settings.admin.model_dump()))
