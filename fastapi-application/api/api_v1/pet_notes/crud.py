"""
Create
Read
Update
Delete
"""

from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.pet_notes.schemas import PetNoteCreate, PetNoteUpdate
from core.models import PetNote
from core.types import UserIdType


async def create_note(
    session: AsyncSession,
    note_create: PetNoteCreate,
    user_id: UserIdType,
) -> PetNote:
    pass


async def read_note(
    session: AsyncSession,
    user_id: UserIdType,
) -> PetNote | None:
    pass


async def read_notes(
    session: AsyncSession,
    user_id: UserIdType,
) -> list[PetNote]:
    pass


async def update_note(
    session: AsyncSession,
    note_update: PetNoteUpdate,
    user_id: UserIdType,
) -> PetNote:
    pass


async def delete_notes(
    session: AsyncSession,
    user_id: UserIdType,
) -> None:
    pass
