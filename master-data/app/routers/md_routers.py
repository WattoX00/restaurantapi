from fastapi import APIRouter
from schemas.md_schemas import MenuRequest
from services.md_services_interface import MenuServiceImpl

from services.md_services_interface import SessionLocal
from db.models import MenuItem

router = APIRouter()

menu_service = MenuServiceImpl()

@router.get("/get_menu")
def get_menu():
    db = SessionLocal()
    items = db.query(MenuItem).all()
    db.close()
    return items

@router.post("/new_item")
def new_item(data: MenuRequest):
    return menu_service.addItems(data)