import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound, DatabaseError

log = logging.getLogger(__name__)


def register_errors_handlers(app: FastAPI) -> None:

    @app.exception_handler(ValidationError)
    def handle_pydantic_validation_error(
        request: Request,
        exc: ValidationError,
    ) -> ORJSONResponse:
        return ORJSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "message": "Unhandled error",
                "error": exc.errors(),
            },
        )

    @app.exception_handler(NoResultFound)
    def handle_sqlalchemy_no_result_found_error(
        request: Request,
        exc: NoResultFound,
    ) -> ORJSONResponse:
        return ORJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "Item not found",
                "error": "Not found",
            },
        )

    @app.exception_handler(DatabaseError)
    def handle_sqlalchemy_database_error(
        request: Request,
        exc: DatabaseError,
    ) -> ORJSONResponse:
        log.error(
            "Unhandled database error",
            exc_info=exc,
        )

        return ORJSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "An unexpected database error has occurred."},
        )
