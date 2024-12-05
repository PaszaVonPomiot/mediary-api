import logging
from enum import IntEnum, StrEnum


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"


class LogLevel(IntEnum):
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET
