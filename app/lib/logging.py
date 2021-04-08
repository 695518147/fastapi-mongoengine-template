# Standard Library Imports
from datetime import datetime
import json
import logging

# 3rd-Party Imports
# None

# App-Local Imports
from app.lib import exit_codes
from app.lib.exceptions import ConfigException
from app.lib.helpers import DATETIME_FORMAT


class JsonFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record: logging.LogRecord) -> str:
        data = {
            "timestamp": datetime.utcnow().strftime(DATETIME_FORMAT),
            "message": record.msg,
            "level": record.levelname,
            "module": record.module,
            "function": record.funcName
        }
        return json.dumps(data)


def init_logging(log_file: str, log_level: str) -> logging.Logger:
    file_handler = logging.FileHandler(log_file)
    try:
        file_handler.setLevel(log_level)
    except ValueError as ve:
        raise ConfigException(
            message="Invalid LOG_LEVEL specified: {log_level}",
            exit_code=exit_codes.E_CONFIG
        ) from ve

    file_handler.setFormatter(JsonFormatter())

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(file_handler)

    return logger
