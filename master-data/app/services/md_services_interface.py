# main logic - calls db

from interface.md_interface import AddMenuItem, MenuItemId
from schemas.md_schemas import MenuRequest, MenuId, MenuItemUpdate

from db.database import SessionLocal
from db.models import MenuItem

# add menu item -> abs -> basemodel

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
        return {"message": "Saved!"}

class MenuGet():

    def getMenuItems(self):
        db = SessionLocal()

        items = db.query(MenuItem).all()

        result = []
        for item in items:
            result.append({
                "id": item.id,
                "food_name": item.food_name,
                "category": item.category,
                "price": item.price,
                "ingredients": item.ingredients,
                "allergies": item.allergies,
                "availability": item.availability
            })
        db.close()
        return result

# delete

class MenuServiceDlt(MenuItemId):

    def menuItemId(self, id: MenuId):
        db = SessionLocal()
        item = db.query(MenuItem).filter(MenuItem.id == id).first()
        if not item:
            db.close()
            return {"Message": "Item Not found"}

        db.delete(item)
        db.commit()
        db.close()
        return {"message": "Item Deleted"}

# update

class MenuServiceUpdate():

    def menuItemId(self, id: MenuId, data: MenuItemUpdate):
        db = SessionLocal()
        item = db.query(MenuItem).filter(MenuItem.id == id).first()

        if not item:
            db.close()
            return {"Message": "Item Not found"}
        
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(item, field, value)

        db.commit()
        db.close()
        return {"message": "Updated"}