from typing import Annotated, Type, TypeVar, Generic

from fastapi import APIRouter, status, Body
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.models import db_helper
from crud.dependencies.current_active_user import get_current_active_user
from crud.dependencies.item_by_id import get_item_by_id
from crud.service import CRUDService

ORMModel = TypeVar("ORMModel", bound=DeclarativeBase)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
ReadSchema = TypeVar("ReadSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class CRUDViewsFactory(Generic[CreateSchema, ReadSchema, UpdateSchema]):
    def __init__(
            self,
            model: Type[ORMModel],
    ):
        self.model = model
        self.crud: CRUDService = CRUDService(self.model)

    def get_router(
            self,
            create_schema: Type[CreateSchema],
            read_schema: Type[ReadSchema],
            update_schema: Type[UpdateSchema],
    ) -> APIRouter:
        router = APIRouter()

        crud = self.crud

        create_schema.model_rebuild()
        read_schema.model_rebuild()
        update_schema.model_rebuild()

        CreateSchema = create_schema
        ReadSchema = read_schema
        UpdateSchema = update_schema

        @router.get(
            "/",
        )
        async def get_entities(
                session: Annotated[
                    AsyncSession,
                    Depends(db_helper.scoped_session_dependency),
                ],
                user=Depends(get_current_active_user),
        ):
            return await crud.read_entities(
                session=session,
                user_id=user.id,
            )

        @router.get(
            "/{item_id}",
            response_model=ReadSchema,
        )
        async def get_entity(
                db_entity=Depends(get_item_by_id(crud=crud)),
        ):
            return db_entity

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
            return await crud.create_entity(
                session=session,
                user_id=user.id,
                create_schema=create_schema,
            )

        @router.patch(
            "/{item_id}",
            response_model=ReadSchema,
        )
        async def update_entity(
                session: Annotated[
                    AsyncSession,
                    Depends(db_helper.scoped_session_dependency),
                ],
                update_schema: UpdateSchema = Body(...),
                db_entity=Depends(get_item_by_id(crud)),
        ):
            return await crud.update_entity(
                session=session,
                db_entity=db_entity,
                update_schema=update_schema,
            )

        @router.delete(
            "/{item_id}",
            status_code=status.HTTP_204_NO_CONTENT,
        )
        async def delete_entity(
                session: Annotated[
                    AsyncSession,
                    Depends(db_helper.scoped_session_dependency),
                ],
                db_entity=Depends(get_item_by_id(crud)),
        ):
            await crud.delete_entity(
                session=session,
                db_entity=db_entity,
            )

        return router
