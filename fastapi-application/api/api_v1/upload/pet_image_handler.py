from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.pets.schemas import PetAvatarUpdate
from core.models import db_helper, Pet
from crud.dependencies.get_service_dependencies import get_update_service_dependency
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.types import ORMService
from s3.client import client

router = APIRouter()


@router.post("/images/pets/{item_id}")
async def set_pet_image(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
    service: Annotated[ORMService, Depends(get_update_service_dependency(Pet))],
    pet: Annotated[Pet, Depends(get_item_by_id(Pet))],
    image: UploadFile,
):

    image_url = await client.upload_file(
        filename=image.filename,
        file=await image.read(),
    )

    update_schema = PetAvatarUpdate(
        image_url=image_url,
    )

    return await service.update_pet(
        session=session,
        entity=pet,
        update_schema=update_schema,
    )
