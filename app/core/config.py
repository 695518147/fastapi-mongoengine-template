# Standard Library Imports
# None

# 3rd-Party Imports
# None

# App-Local Imports
# None

from pydantic import BaseSettings

# READ: https://fastapi.tiangolo.com/advanced/settings/#settings-and-testing
# import os
# print(os.environ.get('TESTING'))


class Settings(BaseSettings):
    API_V1_PATH: str = "/api/v1"
    API_NAME: str = "FastAPI"

    MONGODB_DBNAME: str
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGO_MONITORING: bool = False

    LOG_FILE: str
    LOG_LEVEL: str = "INFO"

    class Config:   # pylint:  disable=too-few-public-methods
        env_file = ".env"


settings = Settings()
