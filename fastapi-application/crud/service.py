"""
Create
Read
Update
Delete
"""

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.types import UserIdType


class CRUDService:
    def __init__(self, model):
        self.model = model

    async def create_entity(
        self,
        session: AsyncSession,
        user_id: UserIdType,
        create_schema,
        **kwargs,
    ):
        db_entity = self.model(**create_schema.model_dump())
        db_entity.user_id = user_id
        session.add(db_entity)
        await session.commit()
        await session.refresh(db_entity)
        return db_entity

    async def read_entities(
        self,
        session: AsyncSession,
        user_id: UserIdType,
        **kwargs,
    ):
        stmt = (
            select(self.model)
            .where(self.model.user_id == user_id)
            .order_by(self.model.id)
        )
        result: Result = await session.execute(statement=stmt)
        entities = list(result.scalars().all())
        return entities

    async def read_entity(
        self,
        session: AsyncSession,
        entity_id,
        **kwargs,
    ):
        db_entity = await session.get(self.model, entity_id)
        return db_entity

    async def update_entity(
        self,
        session: AsyncSession,
        db_entity,
        update_schema,
        **kwargs,
    ):
        for name, value in update_schema.model_dump(exclude_unset=True).items():
            setattr(db_entity, name, value)
        await session.commit()
        return db_entity

    async def delete_entity(
        self,
        session: AsyncSession,
        db_entity,
    ) -> None:
        await session.delete(db_entity)
        await session.commit()
