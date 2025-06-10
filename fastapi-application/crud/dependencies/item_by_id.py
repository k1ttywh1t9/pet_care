from typing import Annotated, TYPE_CHECKING
from fastapi import Path, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper
from core.types import UserIdType
from crud.service import CRUDService

from .current_active_user import get_current_active_user


def get_item_by_id(crud: CRUDService):
    async def dependency(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.scoped_session_dependency),
        ],
        user: Annotated[UserIdType, Depends(get_current_active_user)],
        item_id: Annotated[int, Path],
    ):
        db_entity = await crud.read_entity(
            session=session,
            entity_id=item_id,
        )
        if db_entity:
            if db_entity.user_id == user.id:
                return db_entity
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{crud.model.__tablename__} entity with id {item_id} do not belong to user {user.id}",
            )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{crud.model.__tablename__} entity with id {item_id} not found",
        )

    return dependency
