from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from services.orders_services import AddNewOrder, ViewOrders, ViewOrder, UpdateOrder, FinishOrder
from schemas.orders_schemas import NewOrderElement

from auth.orders_auth import authenticate_user, create_access_token, verify_token

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

add_new_order = AddNewOrder()
view_current_orders = ViewOrders()
view_current_order = ViewOrder()
update_selected_order = UpdateOrder()
finish_order = FinishOrder()

@router.post("/login")
def login(data: LoginData):

    user = authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})

    return {"access_token": token}

@router.post("/add_order")
def add_order(data: NewOrderElement):
    return add_new_order.add_new_order(data)

@router.get("/view_orders")
def view_orders():
    return view_current_orders.view_orders()

@router.get("/view_finished")
def view_finished():
    return view_finished_orders.view_finished_orders()

@router.get("/view_order/{id}")
def view_order(id: int):
    return view_current_order.view_order(id)

@router.patch("/update_odrder/{id}")
def update_order(id: int, data: NewOrderElement, user=Depends(verify_token)):
    return update_selected_order.update_order(id, data)

@router.patch("/finish_order/{id}")
def patch_finish_order(id: int, user=Depends(verify_token)):
    return finish_order.finish_order(id)
