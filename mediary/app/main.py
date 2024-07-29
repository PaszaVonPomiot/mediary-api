import logging

from fastapi import FastAPI

from mediary.app.api.routers import setup_routers

log = logging.getLogger(__name__)
app = FastAPI()

setup_routers(app=app)
