from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from actions.create_superuser import create_superuser
from api import router as api_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    await create_superuser(**settings.admin.model_dump())
    yield
    # on shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(
    router=api_router,
)


@main_app.get("/")
async def index():
    return {"message": "Hello Index!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
