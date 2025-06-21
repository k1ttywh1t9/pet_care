from typing import Annotated, Type

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.base import FactoryBase
from crud_router.elements.types import ORMModel


class DeleteRouterFactory(FactoryBase):
    def get_router(
        self,
    ):
        router = APIRouter()

        service = self.service

        @router.delete(
            "/{item_id}",
            status_code=status.HTTP_204_NO_CONTENT,
        )
        async def delete_entity(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            entity: Annotated[
                Type[ORMModel],
                Depends(get_item_by_id(service)),
            ],
        ):
            await service.delete_entity(
                session=session,
                entity=entity,
            )

        return router
