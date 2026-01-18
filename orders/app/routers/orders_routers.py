from fastapi import APIRouter

from services.orders_services import AddNewOrder
from schemas.orders_schemas import NewOrderElement

router = APIRouter()

add_new_order = AddNewOrder()

@router.post("/add_order")
def add_order(data: NewOrderElement): # abs basemodel
    return add_new_order.add_new_order(data)

@router.get("/view_order")
def view_order():
    pass

@router.patch("/update_odrder/{id}")
def update_order(id: int):
    pass

@router.delete("/finish_order/{id}")
def delete_order(id: int):
    pass