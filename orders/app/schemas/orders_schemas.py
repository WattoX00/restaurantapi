from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime

class NewOrderElement(BaseModel):
    food_names: List[str]
    table_number: int
    description: str
    time: datetime
    finished: bool

class UpdateOrderElement(BaseModel):
    food_names: Optional[List[str]] = None
    table_number: Optional[int] = None
    description: Optional[str] = None
    time: Optional[datetime] = None
    finished: Optional[bool] = None

class OrderId(BaseModel):
    id: int
