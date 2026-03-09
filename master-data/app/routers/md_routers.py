from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from schemas.md_schemas import MenuRequest, MenuItemUpdate
from services.md_services_interface import MenuServiceImpl, MenuGet, MenuServiceDlt, MenuServiceUpdate

from services.md_services_interface import SessionLocal
from db.models import MenuItem

from auth.md_auth import authenticate_user, create_access_token, verify_token

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

menu_service = MenuServiceImpl()
get_menu_items = MenuGet()
delete_menu_item = MenuServiceDlt()
update_menu = MenuServiceUpdate()

@router.post("/login")
def login(data: LoginData):

    user = authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})

    return {"access_token": token}

@router.get("/get_menu")
def get_menu():
    return get_menu_items.getMenuItems()

@router.post("/new_item")
def new_item(data: MenuRequest, user=Depends(verify_token)):
    return menu_service.addItems(data)

@router.delete("/delete_item/{id}")
def delete_item(id: int, user=Depends(verify_token)):
    return delete_menu_item.menuItemId(id)

@router.patch("/patch_item/{id}")
def patch_item(id: int, data: MenuItemUpdate, user=Depends(verify_token)):
    return update_menu.menuItemId(id, data)
