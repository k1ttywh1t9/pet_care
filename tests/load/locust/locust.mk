# tests/load/locust/locust.mk

# Путь относительно корня проекта
LOCUST_FILE := tests/load/locust/tasks/index_flow.py
LOCUST_HOST := http://localhost:8889
LOAD_TEST_FILE = docker-compose/load_tests.yaml

.PHONY: locust-up
locust-up:
	${DC} \
	-f ${LOAD_TEST_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} up --build -d

.PHONY: locust-stop
locust-stop:
	${DC} \
	-f ${LOAD_TEST_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} down

.PHONY: locust-logs
locust-logs:
	${DC} \
	-f ${LOAD_TEST_FILE} \
	-f ${OVERRIDE_FILE} \
	${ENV} logs locust -f