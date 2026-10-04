from fastapi import APIRouter


router = APIRouter(prefix="", tags=["index"])

@router.get("/")
def index():
    return {"hello": "world"}