
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import Courier
from sqlalchemy import select
from sqlalchemy.sql import func
from models import Order
from sqlalchemy.orm import joinedload
from enums.status import Status
from services.avg import avg
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
        """
        Тут я хотел использовать агрегативные функции, все работало успешно в синхронном режиме, но как только прекрутил асинхронный sqlachemy...
        вобщем не удалось завести агрегативные функции
        """
        courier: Courier = await db.get(Courier, id)

        if not courier:
            raise HTTPException(
                status_code=404,
                detail="Courier not found"
            )
            
        result = await db.execute(select(Order).where(Order.courier_id == id))
        orders: Order = result.scalars().all()
        
        avg_order_complete_time = avg.avg_time(orders)
        avg_order_complete_day = avg.avg_day(orders)
        
        active_order = [order for order in orders if order.status == Status.works] 
        
        print(active_order)
        
        response ={
            'active_order': active_order,
            'avg_order_complete_time': avg_order_complete_time, 
            'avg_day_orders': avg_order_complete_day
        }
        return response
    
    