from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship, declarative_base
from models.database import Base

class Courier(Base):
    __tablename__ = 'couriers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    districts = Column(ARRAY(String(20)), index=True)

    orders = relationship("Order", back_populates="user")