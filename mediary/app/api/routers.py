import logging

from fastapi import APIRouter, FastAPI

from mediary.app.api.v1 import core

log = logging.getLogger(__name__)
router_v1 = APIRouter(prefix="/v1")


def setup_routers(app: FastAPI) -> None:
    router_v1.include_router(router=core.router, prefix="/core", tags=["core"])
    app.include_router(router=router_v1)
    log.info("Routers setup complete")
