from typing import Any

from colorlog import ColoredFormatter  # noqa: F401
from pydantic_settings import BaseSettings

from mediary.app.enums import LogLevel


class LoggerSettings:
    LEVEL: LogLevel = LogLevel.INFO
    FORMAT: str = "%(log_color)s%(asctime)s.%(msecs)03d | %(levelname)s | %(name)3s:%(lineno)d | %(message)s"  # noqa: E501

    def get_config(self) -> dict[str, Any]:
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "loggers": {
                "root": {
                    "handlers": ["colored_console"],
                    "level": self.LEVEL,
                },
            },
            "handlers": {
                "colored_console": {
                    "formatter": "colored_verbose",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "level": self.LEVEL,
                },
            },
            "formatters": {
                "colored_verbose": {
                    "class": "colorlog.ColoredFormatter",
                    "format": self.FORMAT,
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },
        }


class DatabaseSettings(BaseSettings):
    NAME: str = "mediary"
    URL: str = "localhost"
    USER: str = ""
    PASS: str = ""


class ModuleSettings:
    logger: LoggerSettings = LoggerSettings()
    db: DatabaseSettings = DatabaseSettings()


settings = ModuleSettings()
