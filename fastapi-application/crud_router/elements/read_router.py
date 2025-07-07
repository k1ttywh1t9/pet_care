from typing import Type, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.base import FactoryBase
from crud_router.elements.types import ReadSchema, ORMModel
from dependencies.current_active_user import get_current_active_user


class ReadRouterFactory(FactoryBase):
    def get_router(
        self,
        read_schema: Type[ReadSchema],
    ):
        router = APIRouter()

        service = self.service

        read_schema.model_rebuild()

        ReadSchema = read_schema

        @router.get(
            "/",
            response_model=list[ReadSchema],
        )
        async def get_entities(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            user=Depends(get_current_active_user),
        ):
            return await service.read_entities(
                session=session,
                user_id=user.id,
            )

        @router.get(
            "/page/{page_number}",
            response_model=list[ReadSchema],
        )
        async def get_paginated_entities(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            page_number: int,
            page_size: int = 100,
            user=Depends(get_current_active_user),
        ):
            return await service.read_paginated_entities(
                session=session,
                user_id=user.id,
                offset=page_number * page_size - page_size,
                limit=page_size,
            )

        @router.get(
            "/{item_id}",
            response_model=ReadSchema,
        )
        async def get_entity(
            entity: Annotated[Type[ORMModel], Depends(get_item_by_id(service=service))],
        ):
            return entity

        return router
