from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class S3Keys(BaseModel):
    access_key: str
    secret_key: str


class S3Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.aws",),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="S3_CONFIG__",
    )

    endpoint_url: str = "https://s3.uz-2.srvstorage.uz"
    region_name: str = "uz-2"
    bucket_name: str = "test-pet-care"
    container_public_domain: str = (
        "https://884735f7-b340-4f03-a358-2f9fdbf28c12.srvstatic.uz"
    )
    keys: S3Keys


s3_config = S3Config()
