from typing import Annotated

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.pets.schemas import PetAvatarUpdate
from core.models import Pet, db_helper
from crud.dependencies.item_by_id import get_item_by_id
from crud.elements.update_service import UpdateService
from s3.client import client

router = APIRouter()


update_pet = UpdateService(
    model=Pet,
).update_entity


@router.post("/set-image/pet/{item_id}")
async def set_pet_image(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
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

    return await update_pet(
        session=session,
        entity=pet,
        update_schema=update_schema,
    )
