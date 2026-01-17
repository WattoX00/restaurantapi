# pydantic basemodel
from pydantic import BaseModel
from enum import Enum
from typing import List

class Allergy(str, Enum):
    nuts = "nuts"
    gluten = "gluten"
    dairy = "dairy"
    
class MenuRequest(BaseModel):
    food_name: str
    category: str
    price: int
    ingredients: List[str]
    allergies: List[Allergy]
    availability: bool