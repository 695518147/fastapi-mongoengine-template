# Standard Library Imports
import logging

# 3rd-Party Imports
from mongoengine import connect
from mongoengine.connection import disconnect_all
from pymongo import monitoring

# App-Local Imports
from app.core import settings

logger = logging.getLogger()


class CommandLogger(monitoring.CommandListener):
    def started(self, event):
        logger.debug(
            "Command {0.command_name} with request id "
            "{0.request_id} started on server "
            "{0.connection_id}".format(event)
        )

    def succeeded(self, event):
        logger.debug(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "succeeded in {0.duration_micros} "
            "microseconds".format(event)
        )

    def failed(self, event):
        logger.debug(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "failed in {0.duration_micros} "
            "microseconds".format(event)
        )


async def mongo_connect():
    if settings.MONGO_MONITORING:
        logger.info(f"configuring mongo command monitoring")
        monitoring.register(CommandLogger())

    logger.info(f"connecting to mongo at {settings.MONGODB_HOST}:{settings.MONGODB_PORT}")
    connect(settings.MONGODB_DBNAME, host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
    logger.info("Connected to mongodb")


async def close_mongo():
    logger.info("Disconnecting from mongo")
    disconnect_all()
