from schemas.orders_schemas import NewOrderElement
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