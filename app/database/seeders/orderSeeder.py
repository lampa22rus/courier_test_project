from faker import Faker
from fastapi import Depends
from sqlalchemy.orm import Session
from database import session_dependency

from database.models.order import Order

def orderSeed(coint,session:Session= Depends(session_dependency)):
    session.commit()