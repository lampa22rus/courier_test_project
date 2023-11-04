from fastapi import FastAPI
from routers.couriers import router as couriers_router
from routers.orders import router as orders_router

app = FastAPI()

app.include_router(
    router=couriers_router,
    prefix='/courier',
)
app.include_router(
    router=orders_router,
    prefix='/order',
)