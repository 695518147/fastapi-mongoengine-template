# Standard Library Imports
# None

# 3rd-Party Imports
from pydantic import BaseModel

# App-Local Imports
# None


class Message(BaseModel):
    message: str
