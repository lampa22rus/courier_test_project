
from models import Courier
from models import Order
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.engine import Result
from enums.status import Status
import datetime


class orderController():

    async def orderCreate(order_in, db: AsyncSession):
        result: Result = await db.execute(select(Courier)
                                          .where(Courier.districts.any(order_in.districts))
                                          .where(Courier.busy == False))
        courier = result.scalars().first()
        if not courier:
            raise HTTPException(
                status_code=404,
                detail="Сourier not found"
            )

        courier.busy = True

        order: Order = Order(
            name=order_in.name,
            districts=order_in.districts,
            courier_id=courier.id,
        )
        db.add(order)
        await db.commit()
        await db.refresh(order)
        return order

    async def orderGet(id, db: AsyncSession):
        order: Order = await db.get(Order, id)

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        return {
            'courier_id': order.courier_id,
            'status': Status(order.status).value
        }

    async def orderUpdate(id, db: AsyncSession):
        result: Result = await db.execute(select(Order)
                                          .where(Order.id == id)
                                          .options(joinedload(Order.courier)))

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        order: Order = result.scalars().first()

        if (order.status == Status.complited):
            raise HTTPException(
                status_code=406,
                detail="The order is completed"
            )

        order.completed_at = datetime.datetime.utcnow()
        order.status = Status.complited
        order.courier.busy = False

        await db.commit()

        return JSONResponse({'msg': 'success'})
