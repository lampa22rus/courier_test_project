from fastapi import APIRouter,Depends
from models.database import session_dependency
from sqlalchemy.ext.asyncio import AsyncSession
from controllers.orderController import orderController
import schemas
from typing import List
router = APIRouter()

# response_model=schemas.orderResponce,
@router.post("/", status_code=201,response_model=schemas.orderResponce)
async def create_order(order_in:schemas.orderCreateValidate,db:AsyncSession= Depends(session_dependency)):
    return await orderController.orderCreate(order_in=order_in,db=db)


@router.get("/{id}", response_model=schemas.orderInfoResponce,status_code=200)
async def get_order(id: int,db:AsyncSession= Depends(session_dependency)):
    return await orderController.orderGet(id=id,db=db)


@router.post("/{id}", status_code=204)
async def update_order(id: int,db:AsyncSession= Depends(session_dependency)):
    return await orderController.orderUpdate(id=id,db=db)