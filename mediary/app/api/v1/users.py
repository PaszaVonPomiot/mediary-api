from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_users_endpoint() -> str:
    return "OK"