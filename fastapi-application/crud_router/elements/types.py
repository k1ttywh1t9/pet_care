from typing import TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from crud.elements.base import ServiceBase

ORMModel = TypeVar("ORMModel", bound=DeclarativeBase)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
ReadSchema = TypeVar("ReadSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)

ORMService = TypeVar("ORMService", bound=ServiceBase)
