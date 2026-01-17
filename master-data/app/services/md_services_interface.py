# main logic - calls db

from interface.md_interface import AddMenuItem
from schemas.md_schemas import MenuRequest

from db.database import SessionLocal
from db.models import MenuItem

class MenuServiceImpl(AddMenuItem):

    def addItems(self, request: MenuRequest):
        db = SessionLocal()
        menu_item = MenuItem(
            food_name=request.food_name,
            category=request.category,
            price=request.price,
            ingredients=request.ingredients,
            allergies=request.allergies,
            availability=request.availability
        )
        db.add(menu_item)
        db.commit()
        db.refresh(menu_item)
        db.close()
        return {"message": "Saved!", "id": menu_item.id}