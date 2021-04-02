# Standard Library Imports
import logging

# 3rd-Party Imports
from mongoengine import connect
from mongoengine.connection import disconnect_all

# App-Local Imports
from app.core import settings

logger = logging.getLogger()

async def mongo_connect():
    logger.info(f"connecting to mongo at {settings.MONGODB_HOST}:{settings.MONGODB_PORT}")
    connect(settings.MONGODB_DBNAME, host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
    logger.info("Connected to mongodb")

async def close_mongo():
    logger.info("Disconnecting from mongo")
    disconnect_all
