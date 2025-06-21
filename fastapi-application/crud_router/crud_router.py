from typing import Generic, Type

from fastapi import APIRouter

from crud_router.elements.base import FactoryBase
from crud_router.elements.create_router import CreateRouterFactory
from crud_router.elements.delete_router import DeleteRouterFactory
from crud_router.elements.read_router import ReadRouterFactory
from crud_router.elements.types import CreateSchema, ReadSchema, UpdateSchema, ORMModel
from crud_router.elements.update_router import UpdateRouterFactory


class CRUDRouterFactory(Generic[CreateSchema, ReadSchema, UpdateSchema], FactoryBase):
    def get_router(
        self,
        create_schema: Type[CreateSchema],
        read_schema: Type[ReadSchema],
        update_schema: Type[UpdateSchema],
    ) -> APIRouter:
        router = APIRouter()

        create_router = CreateRouterFactory(
            self.model,
            self.service,
        ).get_router(
            create_schema=create_schema,
            read_schema=read_schema,
        )

        read_router = ReadRouterFactory(
            self.model,
            self.service,
        ).get_router(
            read_schema=read_schema,
        )

        update_router = UpdateRouterFactory(
            self.model,
            self.service,
        ).get_router(
            update_schema=update_schema,
            read_schema=read_schema,
        )

        delete_router = DeleteRouterFactory(
            self.model,
            self.service,
        ).get_router()

        router.include_router(create_router)
        router.include_router(read_router)
        router.include_router(update_router)
        router.include_router(delete_router)

        return router
