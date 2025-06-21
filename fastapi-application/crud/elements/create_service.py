from sqlalchemy.ext.asyncio import AsyncSession

from core.types import UserIdType
from crud.elements.base import ServiceBase


class CreateService(ServiceBase):
    async def create_entity(
        self,
        session: AsyncSession,
        user_id: UserIdType,
        create_schema,
        **kwargs,
    ):
        entity = self.model(**create_schema.model_dump())
        entity.user_id = user_id
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity
