from pydantic import BaseModel
from typing import List
from enum import Enum

class TimeOfTheDay(str, Enum):
    morning = "morning"
    noon = "noon"
    afternoon = "afternoon" 

class NewOrderElement(BaseModel):
    food_names: List[str]
    table_number: int
    description: str
    time_of_the_day: TimeOfTheDay
