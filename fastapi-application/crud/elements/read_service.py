from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.orm import selectinload

from core.types import UserIdType
from crud.elements.base import ServiceBase


class ReadService(ServiceBase):
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

        for rel in self.model.load_relations:
            stmt = stmt.options(selectinload(getattr(self.model, rel)))

        result: Result = await session.execute(statement=stmt)
        entities = list(result.scalars().all())
        return entities

    async def read_paginated_entities(
        self,
        session: AsyncSession,
        user_id: UserIdType,
        offset: int = 0,
        limit: int = 6,
        **kwargs,
    ):
        stmt = (
            select(self.model)
            .where(self.model.user_id == user_id)
            .offset(offset=offset)
            .limit(limit=limit)
            .order_by(self.model.id)
        )

        for rel in self.model.load_relations:
            stmt = stmt.options(selectinload(getattr(self.model, rel)))

        result: Result = await session.execute(statement=stmt)
        entities = list(result.scalars().all())
        return entities

    async def read_entity(
        self,
        session: AsyncSession,
        entity_id: int,
        **kwargs,
    ):
        # db_entity = await session.get(self.model, entity_id)
        # return db_entity

        stmt = select(self.model).where(self.model.id == entity_id)

        for rel in self.model.load_relations:
            stmt = stmt.options(selectinload(getattr(self.model, rel)))

        res = await session.execute(stmt)
        result = res.scalar_one()
        return result
