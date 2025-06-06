from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Pet
from . import crud
from .dependencies import pet_by_id
from .schemas import PetRead, PetCreate, PetUpdate

router = APIRouter(
    tags=["Pets"],
)


@router.get("/", response_model=list[PetRead])
async def get_pets(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
):
    return await crud.read_pets(session=session)


@router.get("/{pet_id}", response_model=PetRead)
async def get_pet(
    pet: Annotated[
        Pet,
        Depends(pet_by_id),
    ],
):
    return pet


@router.post(
    "/",
    response_model=PetRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_pet(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
    pet_create: PetCreate,
):
    return await crud.create_pet(session=session, pet_create=pet_create)


@router.patch("/{pet_id}", response_model=PetRead)
async def update_pet(
    pet_update: PetUpdate,
    pet: Annotated[
        Pet,
        Depends(pet_by_id),
    ],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
):
    return await crud.update_pet(
        session=session,
        pet=pet,
        pet_update=pet_update,
    )


@router.delete(
    "/{pet_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_pet(
    pet: Annotated[
        Pet,
        Depends(pet_by_id),
    ],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.scoped_session_dependency),
    ],
) -> None:
    await crud.delete_pet(
        session=session,
        pet=pet,
    )
