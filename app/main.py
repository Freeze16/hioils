from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from api.main import api_router
from core.config import settings


FRONTEND_DIR = "frontend"


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    generate_unique_id_function=custom_generate_unique_id,
)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")