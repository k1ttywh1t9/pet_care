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
from .schemas import PetCreate


async def create_pet(session: AsyncSession, pet_create: PetCreate) -> Pet:
    pet: Pet = Pet(**pet_create.model_dump())
    session.add(pet)
    await session.commit()
    # await session.refresh(pet)
    return pet


async def read_pets(session: AsyncSession) -> list[Pet]:
    stmt = select(Pet).order_by(Pet.id)
    result: Result = await session.execute(statement=stmt)
    pets = list(result.scalars().all())
    return pets


async def read_pet(session: AsyncSession, pet_id: int) -> Pet | None:
    return await session.get(Pet, pet_id)


async def update_pet(session: AsyncSession) -> Pet:
    pass


async def delete_pet(session: AsyncSession) -> None:
    pass
