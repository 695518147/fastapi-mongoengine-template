# Standard Library Imports
from typing import (
    Any, 
    Dict, 
    Generic, 
    List, 
    Optional, 
    Type, 
    TypeVar, 
    Union
)

# 3rd-Party Imports
from bson import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from mongoengine.errors import NotUniqueError
from pydantic import BaseModel

# App-Local Imports
from app.database.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, model_id: Any) -> Optional[ModelType]:
        return self.model.objects(pk=ObjectId(model_id))

    def get_multi(self, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return [o for o in self.model.objects[skip:skip+limit]]

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_obj.save()

        return db_obj

    def update(self, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        
        db_obj.save()
        return db_obj

    def remove(self, *, model_id: int) -> ModelType:
        obj = self.model.objects(id=model_id)
        obj.delete()
        return obj
