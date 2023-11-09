from faker import Faker
from fastapi import Depends
from sqlalchemy.orm import Session
from database import session_dependency

from database.models.courier import Courier

def userSeed(coint,db:Session):
    fake = Faker()
    
    for _ in range(coint):   
        courier:Courier = Courier(
            name = fake.name(),
            districts = [fake.city() for _ in range(5)]
        )
        # session.add(courier)
        
    db.commit()