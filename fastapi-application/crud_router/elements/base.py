from typing import Type

from crud_router.elements.types import ORMModel, ORMService


class FactoryBase:
    def __init__(
        self,
        model: Type[ORMModel],
        service: ORMService,
    ):
        self.model = model
        self.service = service
