# Standard Library Imports
# None

# 3rd-Party Imports
from fastapi import APIRouter

# App-Local Imports
from app.api.base import main

api_router = APIRouter()
api_router.include_router(main.router)
