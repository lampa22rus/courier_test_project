# from typing import List, Optional
from pydantic import BaseModel
# import datetime
# # 
class courierBase(BaseModel):
    id: int
    name: str
    
# class orderInfoResponce(BaseModel):
#     courier_id: int
#     status: int
    
# class infoOrderResponce(BaseModel):
#     order_id: int
#     order_name: str
    
# class infoCourierResponce(courierBase):
#     active_order: List[infoOrderResponce] ; None 
#     avg_order_complete_time: datetime
#     avg_day_orders: int

# class orderResponce(BaseModel):
#     order_id:int
#     courier_id:int
    
# class orderCreateValidate(BaseModel):
#     courier_id: int
#     district: str   
    
# class courierCreateValidate(BaseModel):
#     name: str     
#     districts: List[str]
    
#     class Config:
#         orm_mode = True
