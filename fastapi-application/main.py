import uvicorn
from fastapi import FastAPI

from core.config import settings

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
