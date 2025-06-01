from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    yield
    # on shutdown
    await db_helper.dispose()


main_app = FastAPI()
main_app.include_router(
    router=api_router,
)


@main_app.get("/")
async def index():
    return {"message": "Hello Index!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
