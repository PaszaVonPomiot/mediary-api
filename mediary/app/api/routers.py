"""
Routers are defined on 3 levels: app, version, and subject.
Define version levels here and include the subject routers.
Make sure to include routers in the correct order.
First include the subject routers in version routers.
Finally include the version routers in app router.
"""

import logging

from fastapi import APIRouter, FastAPI

from mediary.app.api.v1 import core, users

log = logging.getLogger(__name__)
router_v1 = APIRouter(prefix="/v1")


def setup_routers(app: FastAPI) -> None:
    log.info("Setting up routers")
    router_v1.include_router(
        router=core.router,
        prefix="/core",
        tags=["core"],
    )
    router_v1.include_router(
        router=users.router,
        prefix="/users",
        tags=["users"],
    )
    app.include_router(router=router_v1)
    log.info("Routers setup complete")
