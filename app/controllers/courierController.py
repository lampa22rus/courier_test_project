from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import Courier
from sqlalchemy import select,func
from models import Order
from sqlalchemy.orm import joinedload

class courierController():
    
    async def Create(db, courierData):
        courier: Courier = await db.scalar(select(Courier).where(Courier.name == courierData.name))
        if courier:
            raise HTTPException(
                status_code=409,
                detail="The courier already exists"
            )
            
        courier: Courier = Courier(**courierData.model_dump())
        db.add(courier)
        await db.commit()
        return  JSONResponse({'msg' : 'success'}) 
    
    
    async def showAll(db:AsyncSession):
        result: Result = await db.execute(select(Courier))
        return result.scalars().all()
    
    async def showId(id,db:AsyncSession):
        # result: Result = await db.execute(select(Order)
        #                                   .where(Order.id == id)
        #                                   .options(joinedload(Order.courier)))
        
        # order: Order = result.scalars().first()
        result: Result = await db.execute(funk)
        courier = result.scalars().first()
        
        response ={
            # 'active_order': order,
            'avg_order_complete_time': 'time', #time
            'avg_day_orders': 'int'
        }
        return response