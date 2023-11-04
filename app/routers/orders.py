from fastapi import APIRouter
import schemas

router = APIRouter()


# @router.post("/", response_model=schemas.orderResponce,status_code=201)
# async def read_item(id: int):
#     return {"item_id": id, "name": "first"}


# @router.get("/{id}", response_model=schemas.orderInfoResponce,status_code=200)
# def read_item(id: int):
#     return {"item_id": id, "name": "first"}


# @router.put("/{id}", status_code=204)
# async def read_item(id: int):
#     return {"item_id": id, "name": "first"}