DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
APP_FILE = docker_compose/app.yaml
MONITORING_FILE = docker_compose/monitoring.yaml
OVERRIDE_FILE = docker_compose/docker-compose.override.yaml
LOAD_TEST_FILE = docker_compose/load_tests.yaml
EXEC = docker exec -it
DB_CONTAINER = pet_care_example-db
APP_CONTAINER = pet_care_main-app
MONITORING_CONTAINER = pet_care-prometheus-1
LOGS = docker logs
ENV = --env-file .env

# make storages
.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

# make app
.PHONY: app
app:
	${DC} \
	-f ${STORAGES_FILE} \
	-f ${APP_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} \
	-f ${APP_FILE} \
	-f ${STORAGES_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} down


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f


# make monitoring
.PHONY: monitoring
monitoring:
	${DC} \
	-f ${MONITORING_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} up --build -d

.PHONY: monitoring-down
monitoring-down:
	${DC} \
	-f ${MONITORING_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} down


.PHONY: monitoring-logs
monitoring-logs:
	${LOGS} ${MONITORING_CONTAINER} -f

# make load-test
.PHONY: load-test
load-test:
	${DC} \
	-f ${APP_FILE} \
	-f ${STORAGES_FILE} \
	-f ${MONITORING_FILE} \
	-f ${LOAD_TEST_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} --profile test up load-tester

# make all
.PHONY: all
all: 
	make app && \
	make monitoring

.PHONY: all-down
all-down: 
	make app-down && \
	make monitoring-down
