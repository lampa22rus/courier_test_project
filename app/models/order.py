import datetime
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, TIMESTAMP,DateTime
from sqlalchemy.orm import relationship
from enums.status import Status
from models.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer ,autoincrement=True ,primary_key=True, index=True)
    name = Column(String(20))
    districts = Column(String(20))
    status = Column(Enum(Status),default=Status.works)
    created_at = Column(TIMESTAMP,default=datetime.datetime.utcnow())
    completed_order = Column(DateTime,nullable=True, default=None, index=True)
    courier_id = Column(Integer, ForeignKey("couriers.id"),index=True)
    
    courier = relationship("Courier", back_populates="orders")