from fastapi import APIRouter

from api.api_v1.pet_notes.schemas import PetNoteCreate, PetNoteRead, PetNoteUpdate
from core.models import PetNote
from crud_router import CRUDRouterFactory

router = APIRouter()

crud_router = CRUDRouterFactory(
    model=PetNote,
).get_router(
    create_schema=PetNoteCreate,
    read_schema=PetNoteRead,
    update_schema=PetNoteUpdate,
)

router.include_router(
    router=crud_router,
)
