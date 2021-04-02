# Standard Library Imports
from typing import (
    Dict,
    Generator
)

# 3rd-Party Imports
import pytest
from fastapi.testclient import TestClient

# App-Local Imports
from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def random_product() -> Dict[str, str]:
    return {
        "name": "Test Product",
        "price": 80,
    }
