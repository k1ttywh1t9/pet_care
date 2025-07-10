import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session

from aws.config import s3_config


class S3Client:
    def __init__(
        self,
        access_key: str = s3_config.keys.access_key,
        secret_key: str = s3_config.keys.secret_key,
        endpoint_url: str = s3_config.endpoint_url,
        bucket_name: str = s3_config.bucket_name,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("aws", **self.config) as client:
            yield client

    async def upload_file(
        self,
        filename: str,
        file: bytes,
    ):
        async with self.get_client() as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=file,
            )

        object_url = f"{s3_config.container_public_domain}/{filename}"
        return object_url


client = S3Client()
