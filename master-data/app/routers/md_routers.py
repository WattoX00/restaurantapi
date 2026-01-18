from fastapi import APIRouter
from schemas.md_schemas import MenuRequest, MenuItemUpdate
from services.md_services_interface import MenuServiceImpl, MenuGet, MenuServiceDlt, MenuServiceUpdate

from services.md_services_interface import SessionLocal
from db.models import MenuItem

router = APIRouter()

menu_service = MenuServiceImpl()
get_menu_items = MenuGet()
delete_menu_item = MenuServiceDlt()
update_menu = MenuServiceUpdate()

@router.get("/get_menu")
def get_menu():
    return get_menu_items.getMenuItems()

@router.post("/new_item")
def new_item(data: MenuRequest):
    return menu_service.addItems(data)

@router.delete("/delete_item/{id}")
def delete_item(id: int):
    return delete_menu_item.menuItemId(id)

@router.patch("/patch_item/{id}")
def patch_item(id: int, data: MenuItemUpdate):
    return update_menu.menuItemId(id, data)