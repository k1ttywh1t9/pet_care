from fastapi_users.authentication import (
    AuthenticationBackend,
)

from api.dependencies.authentication.strategy import get_jwt_strategy
from core.authentication.transport import bearer_transport

authentication_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
