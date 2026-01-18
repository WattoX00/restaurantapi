from fastapi import APIRouter

from services.orders_services import AddNewOrder, ViewOrders, ViewOrder
from schemas.orders_schemas import NewOrderElement

router = APIRouter()

add_new_order = AddNewOrder()
view_current_orders = ViewOrders()
view_current_order = ViewOrder()

@router.post("/add_order")
def add_order(data: NewOrderElement): # abs basemodel
    return add_new_order.add_new_order(data)

@router.get("/view_orders")
def view_orders():
    return view_current_orders.view_orders()

@router.get("/view_order/{id}")
def view_order(id: int):
    return view_current_order.view_order(id)

@router.patch("/update_odrder/{id}")
def update_order(id: int):
    pass

@router.delete("/finish_order/{id}")
def delete_order(id: int):
    pass