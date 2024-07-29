from fastapi import APIRouter

router = APIRouter()


@router.get("/keepalive")
def keepalive_endpoint() -> str:
    return "OK"
