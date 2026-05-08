from locust import HttpUser, task, between, events
from prometheus_client import start_http_server, Counter, Histogram

# 1. Объявляем метрики (стандартные для Prometheus)
REQUEST_COUNT = Counter(
    "locust_requests_total",
    "Total number of requests",
    ["method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "locust_request_duration_seconds",
    "Latency of requests in seconds",
    ["method", "endpoint"],
)


# 2. Запускаем сервер метрик при старте Locust
@events.init.add_listener
def on_locust_init(environment, **kwargs):
    # Порт 8000 будет отдавать данные для Prometheus
    start_http_server(8000)


# 3. Хук, который ловит каждый запрос и пишет его в метрики
@events.request.add_listener
def on_request(
    method, name, response_time, response_length, exception, context, **kwargs
):
    status = "success" if exception is None else "failure"
    REQUEST_COUNT.labels(method=method, endpoint=name, http_status=status).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=name).observe(response_time / 1000)


@events.request.add_listener
def on_request(method, name, response_time, response_length, exception, **kwargs):
    # Определяем статус
    status = "success" if exception is None else "failure"
    # Записываем количество (Counter)
    REQUEST_COUNT.labels(method=method, endpoint=name, http_status=status).inc()
    # Записываем задержку (Histogram)
    # Locust дает response_time в миллисекундах, переводим в секунды
    REQUEST_LATENCY.labels(method=method, endpoint=name).observe(response_time / 1000.0)


class HelloWorldUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hello_world(self):
        self.client.get("/")
