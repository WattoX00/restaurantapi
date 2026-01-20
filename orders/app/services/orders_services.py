from fastapi import HTTPException

from schemas.orders_schemas import NewOrderElement, OrderId
from interface.orders_interface import NewOrder
from db.database import SessionLocal
from db.models import Orders
from client.master_data import get_menu_items


class AddNewOrder(NewOrder):
    def add_new_order(self, orderList: NewOrderElement):
        
        menu = get_menu_items()

        menu_by_name = {
            m["food_name"]: m
            for m in menu
        }

        for item_name in orderList.food_names:
            if item_name not in menu_by_name:
                raise HTTPException(400, f"{item_name} not on menu")

            if not menu_by_name[item_name]["availability"]:
                raise HTTPException(400, f"{item_name} not available")

        with SessionLocal() as db:

            new_item = Orders(
                food_names=orderList.food_names,
                table_number=orderList.table_number,
                description=orderList.description,
                time=orderList.time,
                finsihed=orderList.finished
            )

            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            return {"message": "Saved!"}


class ViewOrders():
    
    def view_orders(self):

        with SessionLocal() as db:
            items = db.query(Orders).all()

            list_of_orders = []
            for item in items:
                list_of_orders.append({
                        "id": item.id,
                        "food_names": item.food_names,
                        "table_number": item.table_number,
                        "description": item.description,
                        "time": item.time,
                        "finished": item.finished
                    })

            return list_of_orders


class ViewOrder():
    def view_order(self, id: OrderId):
        
        with SessionLocal() as db:

            item = db.query(Orders).filter(Orders.id == id).first()

            if not item:
                return {"message": "Item Not Found"}

            return item


class UpdateOrder():
    def update_order(self, id: OrderId, orderUpdate: NewOrderElement):
        
        with SessionLocal() as db:
            item = db.query(Orders).filter(Orders.id == id).first()

            if not item:
                return {"message": "Item Not Found"}

            update_data = orderUpdate.model_dump(exclude_unset=True)

            for field, value in update_data.items():
                setattr(item, field, value)

            db.commit()
            return {"message": "Updated"}


class FinishOrder():
    def finish_order(self, id: OrderId):

        with SessionLocal() as db:
            item = db.query(Orders).filter(Orders.id == id).first()

            if not item:
                return {"message": "Item Not Found"}

            item.finished = True
            db.commit()
            return {"message": "Order Finished"}
