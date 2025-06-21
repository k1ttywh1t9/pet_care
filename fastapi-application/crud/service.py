from crud.elements.create_service import CreateService
from crud.elements.delete_service import DeleteService
from crud.elements.read_service import ReadService
from crud.elements.update_service import UpdateService


class CRUDService(CreateService, ReadService, UpdateService, DeleteService):
    pass
