
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from models import Courier
from sqlalchemy import select
from models import Order
from enums.status import Status
from services.avg import avg


class courierController():

    def Create(db:Session, courierData):
        result: Result = db.query(Courier).where(Courier.name == courierData.name).first()
        if result:
            raise HTTPException(
                status_code=409,
                detail="The courier already exists"
            )

        courier: Courier = Courier(**courierData.model_dump())

        db.add(courier)
        db.commit()
        return JSONResponse({'detail': 'success'})

    def showAll(db:Session):
        return db.query(Courier).all()

    def showId(id, db: Session):
        """
        Тут я хотел использовать агрегативные функции, все работало успешно в синхронном режиме, но как только прекрутил асинхронный sqlachemy...
        вобщем не удалось завести агрегативные функции
        """
        courier: Courier = db.get(Courier, id)

        if not courier:
            raise HTTPException(
                status_code=404,
                detail="Courier not found"
            )

        result = db.query(Order).where(Order.courier_id == id)
        orders: Order = result.scalars().all()

        avg_order_complete_time = avg.avg_time(orders)
        avg_order_complete_day = avg.avg_day(orders)

        active_order = [
            order for order in orders if order.status == Status.works]

        print(active_order)

        response = {
            'active_order': active_order,
            'avg_order_complete_time': avg_order_complete_time,
            'avg_day_orders': avg_order_complete_day
        }
        return response
