from core.types import UserIdType


class IdMixin:
    id: int


class UserIdMixin:
    user_id: UserIdType


class PetIdMixin:
    pet_id: int
