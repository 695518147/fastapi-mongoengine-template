# Standard Library Imports
from typing import (
    Dict,
    Generator
)
import random

# 3rd-Party Imports
import pytest
from fastapi.testclient import TestClient
from random_word import RandomWords

# App-Local Imports
from app.core import settings
from app.main import app

#  I'd rather handle this more gracefully in app.core.config
settings.MONGODB_DBNAME = "testing"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    # from mongoengine.connection import _get_db
    from mongoengine.connection import get_db

    # db = _get_db()
    db = get_db()
    db.connection.drop_database('test')
    print("INITIALIZE HERE")


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def random_product() -> Dict[str, str]:
    r = RandomWords()
    return {
        "name": r.get_random_word(),
        "price": 80,
    }


@pytest.fixture(scope="module")
def old_random_product() -> Dict[str, str]:
    return {
        "name": "Test Product",
        "price": random.randint(0, 10000),
    }
