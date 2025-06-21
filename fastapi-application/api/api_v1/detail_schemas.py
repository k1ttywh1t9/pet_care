from api.api_v1.pets.schemas import PetRead
from api.api_v1.pet_notes.schemas import PetNoteRead
from api.api_v1.expense_entries.schemas import ExpenseEntryRead
from api.api_v1.medical_records.schemas import MedicalRecordRead


class PetDetailsRead(PetRead):
    notes: list[PetNoteRead]
    expense_entries: list[ExpenseEntryRead]
    medical_records: list[MedicalRecordRead]

    class Config:
        orm_mode = True


class PetNoteDetailsRead(PetNoteRead):
    pet: PetRead


class ExpenseEntryDetailsRead(ExpenseEntryRead):
    pet: PetRead


class MedicalRecordDetailsRead(MedicalRecordRead):
    pet: PetRead
