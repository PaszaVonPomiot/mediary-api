import logging
import logging.config

from fastapi import FastAPI

from mediary.app.api.routers import setup_routers
from mediary.config.base import settings

logging.config.dictConfig(settings.logger.get_config())
log = logging.getLogger(__name__)
log.info(settings.db.model_dump())  # TODO: fix getting credentials from settings
app = FastAPI()

setup_routers(app)
