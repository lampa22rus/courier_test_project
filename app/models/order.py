import datetime
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP,DateTime
from sqlalchemy.orm import relationship
from enums.status import Status
from models.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer ,autoincrement=True ,primary_key=True, index=True)
    name = Column(String(20),nullable=False)
    districts = Column(String(20),nullable=False)
    status = Column(ENUM(Status,create_type=False),default=Status.works,nullable=True)
    created_at = Column(TIMESTAMP,default=datetime.datetime.utcnow(),nullable=False)
    completed_at = Column(DateTime, default=None, index=True)
    courier_id = Column(Integer, ForeignKey("couriers.id"),index=True,nullable=False)
    
    courier = relationship("Courier", back_populates="active_order")