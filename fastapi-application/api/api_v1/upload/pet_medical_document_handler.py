from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.medical_records.schemas import (
    MedicalRecordDocumentUpdate,
    MedicalRecordRead,
)
from core.config import settings
from core.models import db_helper, MedicalRecord
from crud.dependencies.get_service_dependencies import get_update_service_dependency
from crud.dependencies.item_by_id import get_item_by_id
from crud_router.elements.types import ORMService
from s3.client import client

router = APIRouter(
    prefix=f"{settings.api.v1.files}{settings.api.v1.medical_records}",
)


@router.post("/{item_id}", response_model=MedicalRecordRead)
async def upload_medical_document(
    session: Annotated[AsyncSession, Depends(db_helper.scoped_session_dependency)],
    service: Annotated[
        ORMService, Depends(get_update_service_dependency(MedicalRecord))
    ],
    medical_record: Annotated[MedicalRecord, Depends(get_item_by_id(MedicalRecord))],
    file: UploadFile,
):
    document_url = await client.upload_file(
        filename=file.filename,
        file=await file.read(),
    )

    update_schema = MedicalRecordDocumentUpdate(
        document_url=document_url,
    )

    return await service.update_entity(
        session=session,
        entity=medical_record,
        update_schema=update_schema,
    )
