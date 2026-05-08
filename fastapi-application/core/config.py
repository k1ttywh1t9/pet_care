from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent

# define absolute path to .env
DOTENV_PATH: Path = BASE_DIR / ".env"
DOTENV_EXAMPLE_PATH: Path = BASE_DIR / ".env.example"


class DatabaseConfig(BaseModel):
    # name: str = Field(alias="POSTGRES_DB")
    # user: str = Field(alias="POSTGRES_USER")
    # password: str = Field(alias="POSTGRES_PASSWORD")
    # host: str = Field(alias="POSTGRES_HOST")
    # port: str = Field(alias="POSTGRES_PORT")
    name: str
    user: str
    password: str
    host: str
    port: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Config(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    pets: str = "/pets"
    pet_notes: str = "/pet_notes"
    expense_entries: str = "/expense_entries"
    medical_records: str = "/medical_records"
    images: str = "/images"
    files: str = "/files"


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
    host: str = "0.0.0.0"
    port: str = "9999"


class S3Keys(BaseModel):
    access_key: str
    secret_key: str


class S3Config(BaseModel):
    endpoint_url: str
    region_name: str
    bucket_name: str
    container_public_domain: str
    keys: S3Keys


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(DOTENV_PATH,),
        # env_file=(".env",),
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI_APP_CONFIG__",
        extra="allow",
    )

    db: DatabaseConfig
    run: RunConfig
    access_token: AccessToken
    admin: Admin
    s3: S3Config
    api: ApiConfig = ApiConfig()

    frontend_app_connection_config: FrontendAppConnectionConfig = (
        FrontendAppConnectionConfig()
    )


settings = Settings()
