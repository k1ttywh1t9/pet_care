from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    api_prefix: str = "/api"
    db: DatabaseConfig


settings = Settings()
