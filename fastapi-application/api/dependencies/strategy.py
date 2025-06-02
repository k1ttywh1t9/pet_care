from fastapi_users.authentication import JWTStrategy

from core.config import settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        lifetime_seconds=settings.access_token.lifetime_seconds,
        algorithm="RS256",
        secret=settings.access_token.private_key_path.read_text(),
        public_key=settings.access_token.public_key_path.read_text(),
    )
