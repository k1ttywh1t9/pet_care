DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
MONITORING_FILE = docker_compose/monitoring.yaml
OVERRIDE_FILE = docker_compose/docker-compose.override.yaml
EXEC = docker exec -it
DB_CONTAINER = pet_care_example-db
APP_CONTAINER = pet_care_main-app
MONITORING_CONTAINER = pet_care-prometheus-1
LOGS = docker logs
ENV = --env-file .env

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app
app:
	${DC} \
	-f ${STORAGES_FILE} \
	-f ${APP_FILE} \
	-f ${MONITORING_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: monitoring-logs
monitoring-logs:
	${LOGS} ${MONITORING_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} \
	-f ${APP_FILE} \
	-f ${STORAGES_FILE} \
	-f ${MONITORING_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} down
