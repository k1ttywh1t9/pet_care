from typing import Type

from crud_router.elements.types import ORMModel


class FactoryBase:
    def __init__(
        self,
        model: Type[ORMModel],
    ):
        self.model = model
