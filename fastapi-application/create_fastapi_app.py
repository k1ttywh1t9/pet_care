from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from actions.create_superuser import create_superuser
from core.config import settings
from core.models import db_helper
from error_handlers import register_errors_handlers

origins = [
    f"http://{settings.run.host}",
    f"http://{settings.run.host}:{settings.run.port}",
    f"http://{settings.frontend_app_connection_config.host}",
    f"http://{settings.frontend_app_connection_config.host}:{settings.frontend_app_connection_config.port}",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    await create_superuser(**settings.admin.model_dump())
    yield
    # on shutdown
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_errors_handlers(app)
    return app
