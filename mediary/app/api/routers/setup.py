from fastapi import APIRouter, FastAPI

from mediary.app.api.routers import core

router_v1 = APIRouter(prefix="/v1")


def setup_routers(app: FastAPI) -> None:
    router_v1.include_router(router=core.router, prefix="/core", tags=["core"])
    app.include_router(router=router_v1)
