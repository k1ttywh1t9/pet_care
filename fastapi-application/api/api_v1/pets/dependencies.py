from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.pets import crud
from api.api_v1.users.fastapi_users_routers_helper import current_active_user
from core.models import db_helper, Pet, User


async def pet_by_id(
    pet_id: Annotated[int, Path],
    user: Annotated[User, Depends(current_active_user)],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
) -> Pet:
    pet = await crud.read_pet(session=session, pet_id=pet_id, owner_id=user.id)
    if pet is not None:
        return pet

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Pet {pet_id} is not your pet",
    )
