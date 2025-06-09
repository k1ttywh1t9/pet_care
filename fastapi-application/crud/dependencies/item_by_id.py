from typing import Annotated, TYPE_CHECKING
from fastapi import Path, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper
from crud.service import CRUDService

if TYPE_CHECKING:
    from sqlalchemy.orm import DeclarativeBase

    class EntityModel(DeclarativeBase):
        pass


def get_item_by_id(crud: CRUDService):
    async def dependency(
        item_id: Annotated[int, Path],
        session: Annotated[
            AsyncSession,
            Depends(db_helper.scoped_session_dependency),
        ],
    ) -> "EntityModel":
        db_entity = await crud.read_entity(
            session=session,
            entity_id=item_id,
        )
        if db_entity is not None:
            return db_entity

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{crud.model.__tablename__} entity with id {item_id} not found",
        )

    return dependency
