from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import PetRead, PetCreate

router = APIRouter(
    tags=["Pets"],
)


@router.get("/", response_model=list[PetRead])
async def get_pets(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
):
    return await crud.read_pets(session=session)


@router.get("/{pet_id}", response_model=PetRead)
async def get_pet(
    pet_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
):
    pet = await crud.read_pet(session=session, pet_id=pet_id)
    if pet is not None:
        return pet
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {pet_id} not found",
    )


@router.post("/", response_model=PetRead)
async def create_pet(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
    pet_create: PetCreate,
):
    return await crud.create_pet(session=session, pet_create=pet_create)
