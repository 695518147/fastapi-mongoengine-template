# Standard Library Imports
import logging

# 3rd-Party Imports
from fastapi import APIRouter
from starlette.responses import RedirectResponse

# App-Local Imports
# None

router = APIRouter()
logger = logging.getLogger()


@router.get("/")
def redirect_to_docs() -> RedirectResponse:
    print("hello!!!")
    return RedirectResponse("/docs")
