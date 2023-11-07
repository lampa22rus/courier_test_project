from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY,Boolean
from sqlalchemy.orm import relationship, declarative_base
from models.database import Base

class Courier(Base):
    __tablename__ = 'couriers'
    
    id = Column(Integer,autoincrement=True ,primary_key=True, index=True)
    name = Column(String(20), unique=True,nullable=False)
    busy = Column(Boolean, default=False,nullable=False)
    districts = Column(ARRAY(String(20)), index=True,nullable=False)

    orders = relationship("Order", back_populates="courier")