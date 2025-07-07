import uvicorn

from api import router as api_router
from core.config import settings
from create_fastapi_app import create_app

main_app = create_app()


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
