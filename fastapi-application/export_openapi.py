# scripts/export_openapi.py
import json

from fastapi.openapi.utils import get_openapi

from main import main_app  # ваш FastAPI-app


def dump():
    spec = get_openapi(
        title=main_app.title,
        version=main_app.version,
        routes=main_app.routes,
    )
    # путь в папку фронта, можно относительный
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    dump()
