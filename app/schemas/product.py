# Standard Library Imports
from typing import Optional

# 3rd-Party Imports
from pydantic import BaseModel

# App-Local Imports
# None


class ProductBase(BaseModel):
    name: Optional[str]
    price: Optional[float]


class ProductCreate(ProductBase):
    name: str
    price: float


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    class Config:  # pylint: disable=too-few-public-methods
        orm_mode = True
