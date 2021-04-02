# Standard Library Imports
from typing import Optional

# 3rd-Party Imports
from mongoengine import DoesNotExist

# App-Local Imports
from app.crud.base import CRUDBase
from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate
from app.lib.exceptions import DocumentDoesNotExistException


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get_by_name(self, name: str) -> Optional[Product]:
        try:
            return self.model.objects.get(name=name)
        except DoesNotExist as dne:
            raise DocumentDoesNotExistException from dne


product = CRUDProduct(Product)
