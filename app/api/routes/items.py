from fastapi import APIRouter


router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def index():
    return {"Hello": "World"}
