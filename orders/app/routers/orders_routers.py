
from fastapi import APIRouter

router = APIRouter()

@router.post("/add_order")
def add_order(): # abs basemodel
    pass

@router.get("/view_order")
def view_order():
    pass

@router.patch("/update_odrder/{id}")
def update_order(id: int):
    pass

@router.delete("/finish_order/{id}")
def delete_order(id: int):
    pass