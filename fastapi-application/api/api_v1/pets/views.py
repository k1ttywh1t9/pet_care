from fastapi import APIRouter

from core.models import Pet
from crud import CRUDViewsFactory
from .schemas import PetRead, PetCreate, PetUpdate

router = APIRouter()

crud_router = CRUDViewsFactory(
    model=Pet,
).get_router(
    create_schema=PetCreate,
    read_schema=PetRead,
    update_schema=PetUpdate,
)


router.include_router(
    router=crud_router,
)
