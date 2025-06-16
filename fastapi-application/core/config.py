from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent.parent


class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 5000


class ApiV1Config(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    pets: str = "/pets"
    pet_notes: str = "/pet_notes"
    expense_entries: str = "/expense_entries"
    medical_records: str = "/medical_records"


class ApiConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Config = ApiV1Config()

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.v1.prefix, self.v1.users, self.v1.auth, "/login")
        path = "".join(parts).removeprefix("/")
        return path


class Admin(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = True
    is_verified: bool = True


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"


class FrontendAppConnectionConfig(BaseModel):
    host: str
    port: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI_APP_CONFIG__",
    )

    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    db: DatabaseConfig
    access_token: AccessToken
    admin: Admin
    frontend_app_connection_config: FrontendAppConnectionConfig


settings = Settings()
