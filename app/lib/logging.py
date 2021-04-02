# Standard Library Imports
from datetime import datetime
import json
import logging

# 3rd-Party Imports
# None

# App-Local Imports
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


def init_logging(logfile: str) -> logging.Logger:
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(JsonFormatter())

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger
