from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

# for get menu req

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

# for delete and patch

class MenuId(BaseModel):
    id: int

# for updating the menu

class MenuItemUpdate(BaseModel):
    food_name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[int] = None
    ingredients: Optional[list] = None
    allergies: Optional[list] = None
    availability: Optional[bool] = None