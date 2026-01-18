from schemas.orders_schemas import NewOrderElement, OrderId
from interface.orders_interface import NewOrder
from db.database import SessionLocal
from db.models import Orders

class AddNewOrder(NewOrder):
    def add_new_order(self, orderList: NewOrderElement):

        db = SessionLocal()

        new_item = Orders(
            food_names=orderList.food_names,
            table_number=orderList.table_number,
            description=orderList.description,
            time_of_the_day=orderList.time_of_the_day
        )

        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        db.close()
        return {"message": "Saved!"}
    
class ViewOrders():
    
    def view_orders(self):

        db = SessionLocal()

        items = db.query(Orders).all()

        list_of_orders = []
        for item in items:
            list_of_orders.append({
                    "id": item.id,
                    "food_names": item.food_names,
                    "table_number": item.table_number,
                    "description": item.description,
                    "time_of_the_day": item.time_of_the_day
                })

        db.close()
        return list_of_orders

class ViewOrder():
    def view_order(self, id: OrderId):
        
        db = SessionLocal()

        item = db.query(Orders).filter(Orders.id == id).first()

        if not item:
            db.close()
            return {"message": "Item Not Found"}
        db.close()
        return item
    
class UpdateOrder():
    def update_order(self, id: OrderId, orderUpdate: NewOrderElement):
        
        db = SessionLocal()
        item = db.query(Orders).filter(Orders.id == id).first()

        if not item:
            db.close()
            return {"message": "Item Not Found"}

        update_data = orderUpdate.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(item, field, value)

        db.commit()
        db.close()
        
        return {"message": "Updated"}