from sqlalchemy.orm import Session
from models import Courier
class courierController():
    
    @classmethod
    def courierCreate(db: Session):
        return db.query(Courier).all()
    
    @classmethod
    def courierGet():
        return True
    
    @classmethod
    def couriersGet():
        return True 