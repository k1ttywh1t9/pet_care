FROM python:3.11-slim

WORKDIR /mnt/locust

# Устанавливаем зависимости
RUN pip install --no-cache-dir locust locust-plugins prometheus_client

# Копируем тесты и конфиги
COPY . .

# Locust будет доступен на 8089 (UI) и 8000 (Prometheus метрики)
EXPOSE 8089 8000

ENTRYPOINT ["locust"]