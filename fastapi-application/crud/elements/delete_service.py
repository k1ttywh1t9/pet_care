from sqlalchemy.ext.asyncio import AsyncSession

from crud.elements.base import ServiceBase


class DeleteService(ServiceBase):
    async def delete_entity(
        self,
        session: AsyncSession,
        entity,
    ) -> None:
        await session.delete(entity)
        await session.commit()
