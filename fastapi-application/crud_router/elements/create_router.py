from typing import Type, Annotated

from fastapi import APIRouter, Depends, Body, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud_router.elements.base import FactoryBase
from crud_router.elements.types import CreateSchema, ReadSchema
from dependencies.current_active_user import get_current_active_user


class CreateRouterFactory(FactoryBase):
    def get_router(
        self,
        create_schema: Type[CreateSchema],
        read_schema: Type[ReadSchema],
    ):
        router = APIRouter()

        create_schema.model_rebuild()
        read_schema.model_rebuild()

        CreateSchema = create_schema
        ReadSchema = read_schema

        @router.post(
            "/",
            response_model=ReadSchema,
            status_code=status.HTTP_201_CREATED,
        )
        async def create_entity(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            user=Depends(get_current_active_user),
            create_schema: CreateSchema = Body(...),
        ):
            return await self.service.create_entity(
                session=session,
                user_id=user.id,
                create_schema=create_schema,
            )

        return router
