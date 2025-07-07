from typing import Annotated, Type

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.dependencies.get_service_dependencies import get_delete_service_dependency
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.base import FactoryBase
from crud_router.elements.types import ORMModel, ORMService


class DeleteRouterFactory(FactoryBase):
    def get_router(
        self,
    ) -> APIRouter:
        router = APIRouter()

        model = self.model

        @router.delete(
            "/{item_id}",
            status_code=status.HTTP_204_NO_CONTENT,
        )
        async def delete_entity(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            service: Annotated[
                ORMService,
                Depends(get_delete_service_dependency(model)),
            ],
            entity: Annotated[
                Type[ORMModel],
                Depends(get_item_by_id(model)),
            ],
        ):
            await service.delete_entity(
                session=session,
                entity=entity,
            )

        return router
