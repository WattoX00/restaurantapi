# main logic - calls db

from interface.md_interface import AddMenuItem
from schemas.md_schemas import MenuRequest

class MenuServiceImpl(AddMenuItem):

    def addItems(self, request: MenuRequest):
        return {
            "food_name": request.food_name,
            "category": request.category,
            "price": request.price,
            "ingredients": request.ingredients,
            "allergies": request.allergies,
            "availability": request.availability
        }
