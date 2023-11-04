from fastapi import APIRouter, Query
from typing import Union
from typing_extensions import Annotated
import schemas

router = APIRouter()

@router.get("/",status_code=201,response_model=schemas.courierBase )
def read_item():
    return {"id": 1, "name": "first"}

# @router.get("/" , response_model=schemas.courierBase , status_code=200)
# def items():
#     return [{"id": 1, "name": "first"}]

# @router.get("/{id}",response_model=schemas.infoCourierResponce,status_code=200)
# def read_item(id: int):
#     return {"item_id": id, "name": "first"}



