from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import datetime

class NewOrderElement(BaseModel):
    food_names: List[str]
    table_number: int
    description: str
    time: datetime
    finished: bool

class OrderId(BaseModel):
    id: int