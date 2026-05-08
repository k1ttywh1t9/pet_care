include tests/load/load_testing.mk

DC = docker compose

# Directories paths variables
PROJECT_DIR = .
DOCKER_COMPOSE_DIR = ./docker-compose

# Files paths variables
NETWORKS_FILE = $(DOCKER_COMPOSE_DIR)/networks.yaml
STORAGES_FILE = ${DOCKER_COMPOSE_DIR}/storages.yaml
APP_FILE = ${DOCKER_COMPOSE_DIR}/app.yaml
MONITORING_FILE = ${DOCKER_COMPOSE_DIR}/monitoring.yaml
OVERRIDE_FILE = ${DOCKER_COMPOSE_DIR}/docker-compose.override.yaml

# Containers names variables
DB_CONTAINER = postgres-db
APP_CONTAINER = main-app

# Commands variables
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env

# Networks management (Infra)
# Make networks once. If exist - nothing happens.
# Delete network only when clear all.
.PHONY: network-up network-down
network-up:
	${DC} -f ${NETWORKS_FILE} ${ENV} create
network-down:
	${DC} -f ${NETWORKS_FILE} ${ENV} down


# make storages
.PHONY: storages storages-down storages-logs
storages: network-up
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down

storages-logs:
	${LOGS} ${DB_CONTAINER} -f

# make app
.PHONY: app app-down app-logs
app: network-up
	${DC} \
	-f ${STORAGES_FILE} \
	-f ${APP_FILE} \
	${ENV} up --build -d

app-down:
	${DC} \
	-f ${APP_FILE} \
	-f ${STORAGES_FILE} \
	${ENV} down

app-logs:
	${LOGS} ${APP_CONTAINER} -f


# make monitoring
.PHONY: monitoring monitoring-down monitoring-logs
monitoring: network-up
	${DC} \
	-f ${MONITORING_FILE} \
	${ENV} up --build -d

monitoring-down:
	${DC} \
	-f ${MONITORING_FILE} \
	${ENV} down

monitoring-logs:
	${LOGS} -f prometheus-metrics

# make all
.PHONY: all all-down
all: 
	make app && \
	make monitoring

all-down: 
	make app-down && \
	make monitoring-down


# Специальная команда для полной зачистки
.PHONY: prune
prune: all-down network-down