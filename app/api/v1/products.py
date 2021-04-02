from typing import Any, List
import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()
logger = logging.getLogger()


@router.get("", response_model=List[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all products.
    """
    products = crud.product.get_multi(skip=skip, limit=limit)
    return products


@router.post("", response_model=schemas.ProductResponse)
def create_product(*, product_in: schemas.ProductCreate) -> Any:
    """
    Create new products.
    """
    product = crud.product.create(obj_in=product_in)
    return product


@router.put("", response_model=schemas.ProductResponse)
def update_product(*, product_in: schemas.ProductUpdate) -> Any:
    """
    Update existing products.
    """
    product = crud.product.get_by_name(model_id=product_in.id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    product = crud.product.update(db_obj=product, obj_in=product_in)
    return product


@router.delete("", response_model=schemas.Message)
def delete_product(*, id: int) -> Any:
    """
    Delete existing product.
    """
    product = crud.product.get(model_id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    crud.product.remove(model_id=product.id)
    return {"message": f"Product with ID = {id} deleted."}
