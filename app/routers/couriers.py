from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from models.database import session_dependency

from controllers.courierController import courierController

import schemas

from typing import List

router = APIRouter()

@router.post("/",status_code=201)
async def courier_create(courierData: schemas.courierCreate,db:AsyncSession= Depends(session_dependency)):
    return await courierController.Create(courierData=courierData,db=db)

@router.get("/" , response_model=List[schemas.courierBase] , status_code=200)
async def show_all(db:AsyncSession= Depends(session_dependency)):
    return await courierController.showAll(db=db)


@router.get("/{id}",response_model=schemas.infoCourierResponce,status_code=200)
async def showId(id: int,db:AsyncSession= Depends(session_dependency)):
    return await courierController.showId(id=id,db=db)


