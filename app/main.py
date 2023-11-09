from fastapi import FastAPI
from database.seeders.seeder import seeder
from routers.couriers import router as couriers_router
from routers.orders import router as orders_router
import uvicorn
import argparse

# args
parser = argparse.ArgumentParser()
parser.add_argument('--server')

# fastapi
app = FastAPI()

app.include_router(
    router=couriers_router,
    prefix='/courier',
)
app.include_router(
    router=orders_router,
    prefix='/order',
)



def parse_arg():
    
    args = parser.parse_args()
    if(args.server == "start"):
       uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
       
    if(args.server == "seed"):
        seeder.run()
    
if __name__ == "__main__":
    parse_arg()