from crud.elements.create_service import CreateService
from crud.elements.delete_service import DeleteService
from crud.elements.read_service import ReadService
from crud.elements.update_service import UpdateService
from crud_router.elements.types import ORMModel


def get_create_service_dependency(
    model: ORMModel,
):
    def dependency():
        service = CreateService(
            model=model,
        )

        return service

    return dependency


def get_read_service_dependency(
    model: ORMModel,
):
    def dependency():
        service = ReadService(
            model=model,
        )

        return service

    return dependency


def get_update_service_dependency(
    model: ORMModel,
):
    def dependency():
        service = UpdateService(
            model=model,
        )

        return service

    return dependency


def get_delete_service_dependency(
    model: ORMModel,
):
    def dependency():
        service = DeleteService(
            model=model,
        )

        return service

    return dependency
