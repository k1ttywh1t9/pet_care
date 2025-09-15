#!/usr/bin/env bash

set -e

# if [ -d "/certs" ]; then
#   echo "certs exist"
# else
#   echo "creating certs"
#   mkdir certs
#   cd certs
#   echo "Generate an RSA private key, of size 2048"
#   openssl genrsa -out jwt-private.pem 2048
#   echo "Extract the public key from the key pair, which can be used in a certificate"
#   openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
#   cd ..
# fi


cd fastapi-application
echo "Run apply migrations.."
alembic upgrade head
echo "Migrations applied!"
cd ..

exec "$@"
