from fastapi import Depends
from sqlalchemy.orm import Session
from database import session_dependency
from database.seeders.courierSeeder import userSeed
from database.seeders.orderSeeder import orderSeed
class seeder():
    def run():
        db:Session=Depends(session_dependency)
        userSeed(coint=10,db=db)

        

    