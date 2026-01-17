from fastapi import APIRouter
from schemas.md_schemas import MenuRequest
from services.md_services_interface import MenuServiceImpl

router = APIRouter()

menu_service = MenuServiceImpl()

@router.get("/get_menu")
def get_menu(data: MenuRequest):
    return {"asd"}


@router.post("/new_item")
def new_item(data: MenuRequest): # basemodel from somewhere -> abs
    return menu_service.addItems(data)