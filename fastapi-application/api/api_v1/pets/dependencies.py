from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.pets import crud
from core.models import db_helper, Pet


async def pet_by_id(
    pet_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
) -> Pet:
    pet = await crud.read_pet(session=session, pet_id=pet_id)
    if pet is not None:
        return pet

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {pet_id} not found",
    )
