FROM python:3.12.11-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel "poetry==2.1.3" urllib3

RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock prestart.sh ./

RUN poetry install --no-root --no-interaction

COPY fastapi-application ./fastapi-application

RUN sed -i 's/\r$//' prestart.sh
RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]
CMD ["python", "fastapi-application/main.py"]