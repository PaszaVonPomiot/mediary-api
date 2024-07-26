from fastapi import APIRouter

router = APIRouter()


@router.get("/keepalive")
def keepalive_endpoint() -> str:
    return "OK"


@router.get("/keepdead")
def keepdead_endpoint() -> str:
    return "NOK"
