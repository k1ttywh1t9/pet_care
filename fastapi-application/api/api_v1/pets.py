from fastapi import APIRouter

from .schemas import PetCreate, PetRead

router = APIRouter(
    prefix="/pets",
    tags=["Pets"],
)


@router.get("/{id}")
async def read_pet(id):
    pet = PetRead(id=id, name="Susie", owner_id=1)
    return {"pet": pet}


@router.post("")
async def create_pet(pet: PetCreate):
    return {"pet_created": PetRead(**pet.model_dump())}
