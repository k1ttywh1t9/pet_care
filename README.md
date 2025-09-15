# Pet care application w/ Postgres

## Requirements

- [Docker](https://www.docker.com/get-started)
- [GNU Make](https://www.gnu.org/software/make/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/k1ttywh1t9/pet_care.git
cd pet_care
```

### 2. Set up environment variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```ini
# FastAPI
FASTAPI_APP_CONFIG__RUN__HOST=0.0.0.0
FASTAPI_APP_CONFIG__RUN__PORT=8000

FASTAPI_APP_CONFIG__ACCESS_TOKEN__reset_password_token_secret=token
FASTAPI_APP_CONFIG__ACCESS_TOKEN__verification_token_secret=token

FASTAPI_APP_CONFIG__ADMIN__EMAIL=admin@example.com
FASTAPI_APP_CONFIG__ADMIN__PASSWORD=admin

# Database
POSTGRES_DB=yourdbname
POSTGRES_USER=yourdbuser
POSTGRES_PASSWORD=yourdbpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432

# AWS S3
S3_CONFIG__KEYS__access_key=key
S3_CONFIG__KEYS__secret_key=key
```

### 3. Create JWT certificates

open console in the project root then paste:

```bash
echo "creating certs"
mkdir certs
cd certs
echo "Generate an RSA private key, of size 2048"
openssl genrsa -out jwt-private.pem 2048
echo "Extract the public key from the key pair, which can be used in a certificate"
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
cd ..
```


### 4. Build and start the containers

```bash
make app
```

This will:
- Build the Docker images
- Start the Django and PostgreSQL containers
- Run migrations
- Create a superuser (if not exists)

### 5. Access the application

- Fastapi development server: http://localhost:8000
- OpenAPI docs: http://localhost:8000/docs
- PostgreSQL: accessible on port 5432 (from within Docker network)

## Makefile Commands

The project includes a Makefile with common commands:

| Command               | Description                                      |
|-----------------------|--------------------------------------------------|
| `make app`            | Build and start containers in detached mode      |
| `make app-down`       | Stop and remove containers                       | 

## Project Structure

```

```

## Database Configuration

The project is pre-configured to use PostgreSQL with these default settings (can be changed in .env):

- Database: `yourdbname`
- User: `yourdbuser`
- Password: `yourdbpassword`
- Host: `db` (Docker service name)
- Port: `5432`

## Deployment

For production deployment:



```bash

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)








SQLAlchemy create engine https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
- Python typing https://docs.python.org/3/library/typing.html
- pydantic settings dotenv https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
- pydantic settings env variables https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values
- pydantic settings env
  variables https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values
- case converter https://github.com/mahenzon/ri-sdk-python-wrapper/blob/master/ri_sdk_codegen/utils/case_converter.py
- SQLAlchemy constraint naming conventions https://docs.sqlalchemy.org/en/20/core/constraints.html#constraint-naming-conventions
- SQLAlchemy constraint naming
  conventions https://docs.sqlalchemy.org/en/20/core/constraints.html#constraint-naming-conventions
- Alembic cookbook https://alembic.sqlalchemy.org/en/latest/cookbook.html
- Alembic naming conventions https://alembic.sqlalchemy.org/en/latest/naming.html#integration-of-naming-conventions-into-operations-autogenerate
- Alembic naming
  conventions https://alembic.sqlalchemy.org/en/latest/naming.html#integration-of-naming-conventions-into-operations-autogenerate
- Alembic + asyncio recipe https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
- orjson https://github.com/ijl/orjson
- FastAPI ORJSONResponse https://fastapi.tiangolo.com/advanced/custom-response/#use-orjsonresponseAdd commentMore actions

```shell
python -c 'import secrets; print(secrets.token_hex())'
```