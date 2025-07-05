from pydantic import ConfigDict

from api.api_v1.pets.schemas import PetRead
from api.api_v1.pet_notes.schemas import PetNoteRead
from api.api_v1.expense_entries.schemas import ExpenseEntryRead
from api.api_v1.medical_records.schemas import MedicalRecordRead


class PetDetailsRead(PetRead):
    notes: list[PetNoteRead]
    expense_entries: list[ExpenseEntryRead]
    medical_records: list[MedicalRecordRead]

    model_config = ConfigDict(from_attributes=True)


class PetNoteDetailsRead(PetNoteRead):
    pet: PetRead

    model_config = ConfigDict(from_attributes=True)


class ExpenseEntryDetailsRead(ExpenseEntryRead):
    pet: PetRead

    model_config = ConfigDict(from_attributes=True)


class MedicalRecordDetailsRead(MedicalRecordRead):
    pet: PetRead

    model_config = ConfigDict(from_attributes=True)
