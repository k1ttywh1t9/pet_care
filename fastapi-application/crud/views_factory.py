from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.dependencies.item_by_id import get_item_by_id
from crud.service import CRUDService

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


class CRUDViewsFactory:
    def __init__(
        self,
        model: "EntityModel",
    ):
        self.model = model
        self.crud: CRUDService = CRUDService(self.model)

    def get_router(
        self,
        create_schema: "EntityCreateSchema",
        read_schema: "EntityReadSchema",
        update_schema: "EntityUpdateSchema",
    ):
        router = APIRouter()

        crud = self.crud

        @router.get(
            "/",
            response_model=list["EntityReadSchema"],
        )
        async def get_entities(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
        ):
            return await crud.read_entities(
                session=session,
            )

        @router.get(
            "/{item_id}",
            response_model="EntityReadSchema",
        )
        async def get_entity(
            db_entity: Annotated[
                "EntityModel",
                Depends(get_item_by_id(crud=crud)),
            ],
        ):
            return db_entity

        @router.post(
            "/",
            response_model="EntityReadSchema",
            status_code=status.HTTP_201_CREATED,
        )
        async def create_entity(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            create_schema: "EntityCreateSchema",
        ):
            return await crud.create_entity(
                session=session,
                create_schema=create_schema,
            )

        @router.patch(
            "/{item_id}",
            response_model="EntityReadSchema",
        )
        async def update_entity(
            session: Annotated[
                AsyncSession,
                Depends(db_helper.scoped_session_dependency),
            ],
            update_schema: "EntityUpdateSchema",
            db_entity: Annotated[
                "EntityModel",
                Depends(get_item_by_id(crud)),
            ],
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
            db_entity: Annotated["EntityModel", Depends(get_item_by_id(crud))],
        ):
            await crud.delete_entity(
                session=session,
                db_entity=db_entity,
            )

        return router
