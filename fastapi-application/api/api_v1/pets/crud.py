"""
Create
Read
Update
Delete
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.models import Pet
from core.types import UserIdType
from .schemas import PetCreate, PetUpdate, PetRead


async def create_pet(
    session: AsyncSession,
    pet_create: PetCreate,
    owner_id: UserIdType,
) -> Pet:
    pet: Pet = Pet(**pet_create.model_dump())
    pet.owner_id = owner_id
    session.add(pet)
    await session.commit()
    # await session.refresh(pet)
    return pet


async def read_pets(
    session: AsyncSession,
    owner_id: UserIdType,
) -> list[Pet]:
    stmt = select(Pet).where(Pet.owner_id == owner_id).order_by(Pet.id)
    result: Result = await session.execute(statement=stmt)
    pets = list(result.scalars().all())
    return pets


async def read_pet(session: AsyncSession, pet_id: int) -> Pet | None:
    return await session.get(Pet, pet_id)


async def update_pet(
    session: AsyncSession,
    pet: Pet,
    pet_update: PetUpdate,
) -> Pet:
    for name, value in pet_update.model_dump(exclude_unset=True).items():
        setattr(pet, name, value)
    await session.commit()
    return pet


async def delete_pet(session: AsyncSession, pet: Pet) -> None:
    await session.delete(pet)
    await session.commit()
