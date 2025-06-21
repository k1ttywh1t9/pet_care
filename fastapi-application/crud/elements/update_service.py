from sqlalchemy.ext.asyncio import AsyncSession

from crud.elements.base import ServiceBase


class UpdateService(ServiceBase):
    async def update_entity(
        self,
        session: AsyncSession,
        entity,
        update_schema,
        **kwargs,
    ):
        for name, value in update_schema.model_dump(exclude_unset=True).items():
            setattr(entity, name, value)
        await session.commit()
        return entity
