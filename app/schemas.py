from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import time
class courierBase(BaseModel):
    id: int
    name: str
    
class orderInfoResponce(BaseModel):
    courier_id: int
    status: int
    
class infoOrderResponce(BaseModel):
    order_id: int
    order_name: str
    
class infoCourierResponce(courierBase):
    active_order: List[infoOrderResponce] = []
    avg_order_complete_time: time
    avg_day_orders: int

class orderResponce(BaseModel):
    order_id:int = Field(..., alias='id')
    courier_id:int
  
    class Config:
        allow_population_by_field_name = True
    

class orderCreateValidate(BaseModel):
    name: str
    districts: str

class courierCreateValidate(BaseModel):
    name: str 
    districts: List[str]
    
    # class Config:
    #     orm_mode = True
    
class showAll(BaseModel):
    Dict[str,courierBase]
    class Config:
        orm_mode = True
        
courierCreate = courierCreateValidate



# from typing import List, Optional, Dict
# from pydantic import BaseModel, Field
# from datetime import time
# from typing import Annotated
# from annotated_types import MinLen, MaxLen
# class courierBase(BaseModel):
#     id: int
#     name: Annotated[str,MinLen(3),MaxLen(20)]
    
# class orderInfoResponce(BaseModel):
#     courier_id: int
#     status: int
    
# class infoOrderResponce(BaseModel):
#     order_id: int
#     order_name: str
    
# class infoCourierResponce(courierBase):
#     active_order: List[infoOrderResponce] = None
#     avg_order_complete_time: time
#     avg_day_orders: int

# class orderResponce(BaseModel):
#     order_id:int = Field(..., alias='id')
#     courier_id:int
  
#     class Config:
#         allow_population_by_field_name = True
    

# class orderCreateValidate(BaseModel):
#     name: Annotated[str,MinLen(3),MaxLen(20)]
#     districts: str

# class courierCreateValidate(BaseModel):
#     name: Annotated[str,MinLen(3),MaxLen(20)]    
#     districts: List[str]
    
#     # class Config:
#     #     orm_mode = True
    
# class showAll(BaseModel):
#     Dict[str,courierBase]
#     class Config:
#         orm_mode = True
        
# courierCreate = courierCreateValidate