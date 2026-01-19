from fastapi import APIRouter

from services.orders_services import AddNewOrder, ViewOrders, ViewOrder, UpdateOrder, FinishOrder
from schemas.orders_schemas import NewOrderElement

router = APIRouter()

add_new_order = AddNewOrder()
view_current_orders = ViewOrders()
view_current_order = ViewOrder()
update_selected_order = UpdateOrder()
finish_order = FinishOrder()

@router.post("/add_order")
def add_order(data: NewOrderElement):
    return add_new_order.add_new_order(data)

@router.get("/view_orders")
def view_orders():
    return view_current_orders.view_orders()

@router.get("/view_order/{id}")
def view_order(id: int):
    return view_current_order.view_order(id)

@router.patch("/update_odrder/{id}")
def update_order(id: int, data: NewOrderElement):
    return update_selected_order.update_order(id, data)

@router.delete("/finish_order/{id}")
def delete_order(id: int):
    return finish_order.finish_order(id)