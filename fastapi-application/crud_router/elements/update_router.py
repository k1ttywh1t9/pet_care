from typing import Type, Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.base import FactoryBase
from crud_router.elements.types import UpdateSchema, ReadSchema, ORMModel


class UpdateRouterFactory(FactoryBase):
    def get_router(
        self,
        update_schema: Type[UpdateSchema],
        read_schema: Type[ReadSchema],
    ):
        router = APIRouter()

        service = self.service

        update_schema.model_rebuild()
        read_schema.model_rebuild()

        UpdateSchema = update_schema
        ReadSchema = read_schema

        @router.patch(
            "/{item_id}",
            response_model=ReadSchema,
        )
        async def update_entity(
            session: Annotated[
                AsyncSession, Depends(db_helper.scoped_session_dependency)
            ],
            update_schema: UpdateSchema,
            entity: Annotated[
                Type[ORMModel],
                Depends(get_item_by_id(service)),
            ],
        ):
            return await service.update_entity(
                session=session,
                entity=entity,
                update_schema=update_schema,
            )

        return router
