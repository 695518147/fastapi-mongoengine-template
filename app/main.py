# Standard Library Imports
# None

# 3rd-Party Imports
from fastapi import FastAPI
import uvicorn

# App-Local Imports
from app.api.v1 import api_router
from app.core import settings
from app.database.session import (
    mongo_connect,
    close_mongo
)
from app.lib.logging import init_logging

logger = init_logging(settings.LOGFILE)
logger.info(f"{settings.PROJECT_NAME} is spinning up.")

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_event_handler("startup", mongo_connect)
app.add_event_handler("shutdown", close_mongo)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
