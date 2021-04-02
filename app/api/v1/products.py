# Standard Library Imports
from typing import (
    Any,
    List
)
import logging

# 3rd-Party Imports
from fastapi import (
    APIRouter,
    HTTPException,
    status
)

# App-Local Imports
from app import schemas, crud
from app.lib.exceptions import DocumentDoesNotExistException

router = APIRouter()
logger = logging.getLogger()


@router.get("/{product_name}", response_model=schemas.ProductResponse)
def get_product(product_name: str) -> Any:
    """
    Retrieve a single product.
    """
    try:
        product = crud.product.get_by_name(name=product_name)
    except DocumentDoesNotExistException as ddnee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"product '{product_name}' does not exist"
        ) from ddnee

    return product


@router.get("", response_model=List[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all products.
    """
    products = crud.product.get_multi(skip=skip, limit=limit)
    print(products)
    return products


@router.post("", response_model=schemas.ProductResponse)
def create_product(*, product_in: schemas.ProductCreate) -> Any:
    """
    Create new products.
    """
    product = crud.product.create(obj_in=product_in)
    return product


@router.put("/{product_name}", response_model=schemas.ProductResponse)
def update_product(*, product_name: str, product_in: schemas.ProductUpdate) -> Any:
    """
    Update existing products.
    """
    try:
        product = crud.product.get_by_name(name=product_name)
    except DocumentDoesNotExistException as ddnee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"product '{product_name}' does not exist"
        ) from ddnee

    product = crud.product.update(db_obj=product, obj_in=product_in)
    return product


@router.delete("/{product_name}", response_model=schemas.Message)
def delete_product(*, product_name: str) -> Any:
    """
    Delete existing product.
    """
    try:
        product = crud.product.get_by_name(name=product_name)
    except DocumentDoesNotExistException as ddnee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"product '{product_name}' does not exist"
        ) from ddnee

    crud.product.remove(model_id=product.id)
    return {"message": f"product {product_name} deleted."}
