from fastapi import APIRouter

from api.routes import items, index

api_router = APIRouter()
api_router.include_router(items.router)
api_router.include_router(index.router)
