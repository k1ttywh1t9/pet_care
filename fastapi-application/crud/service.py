"""
Create
Read
Update
Delete
"""

from typing import TYPE_CHECKING

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeBase
    from pydantic import BaseModel

    class EntityModel(DeclarativeBase):
        pass

    class EntitySchema(BaseModel):
        pass

    class EntityCreateSchema(EntitySchema):
        pass

    class EntityReadSchema(EntitySchema):
        pass

    class EntityUpdateSchema(EntityCreateSchema):
        pass


class CRUDService:
    def __init__(self, model):
        self.model = model

    async def create_entity(
        self,
        session: AsyncSession,
        create_schema: "EntityCreateSchema",
        **kwargs,
    ) -> "EntityModel":
        db_entity = self.model(**create_schema.model_dump())
        session.add(db_entity)
        await session.commit()
        await session.refresh(db_entity)
        return db_entity

    async def read_entities(
        self,
        session: AsyncSession,
        **kwargs,
    ) -> list["EntityModel"]:
        stmt = select(self.model).order_by(self.model.id)
        result: Result = await session.execute(statement=stmt)
        entities = list(result.scalars().all())
        return entities

    async def read_entity(
        self,
        session: AsyncSession,
        entity_id,
        **kwargs,
    ) -> "EntityModel" | None:
        db_entity = await session.get(self.model, entity_id)
        return db_entity

    async def update_entity(
        self,
        session: AsyncSession,
        db_entity: "EntityModel",
        update_schema: "EntityUpdateSchema",
        **kwargs,
    ) -> "EntityModel":
        for name, value in update_schema.model_dump(exclude_unset=True).items():
            setattr(db_entity, name, value)
        await session.commit()
        return db_entity

    async def delete_entity(
        self,
        session: AsyncSession,
        db_entity: "EntityModel",
    ) -> None:
        await session.delete(db_entity)
        await session.commit()
