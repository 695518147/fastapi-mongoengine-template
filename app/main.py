# Standard Library Imports
import sys

# 3rd-Party Imports
from fastapi import FastAPI
import uvicorn

# App-Local Imports
from app.api.base import api_router as base_router
from app.api.v1 import api_router
from app.core import settings
from app.database.session import (
    mongo_connect,
    close_mongo
)
from app.lib.exceptions import ConfigException
from app.lib.logging import init_logging

try:
    logger = init_logging(settings.LOG_FILE, settings.LOG_LEVEL)
except ConfigException as ce:
    print(ce.message)
    sys.exit(ce.exit_code)

logger.info(f"{settings.API_NAME} is spinning up.")

app = FastAPI(title=settings.API_NAME)

# This just creates a redirect to /docs
app.include_router(base_router, prefix="")

# The actual API
app.include_router(api_router, prefix=settings.API_V1_PATH)

# Database connect / disconnect
app.add_event_handler("startup", mongo_connect)
app.add_event_handler("shutdown", close_mongo)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
