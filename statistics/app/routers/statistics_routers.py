from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from datetime import date
from services.statistics_services import MostSoldItems, LeastItemsSold, MonthlyData

from auth.statistics_auth import authenticate_user, create_access_token, verify_token

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

most_sold_items_list = MostSoldItems()
least_sold_items_list = LeastItemsSold()
monthly_data_list = MonthlyData()

@router.post("/login")
def login(data: LoginData):

    user = authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})

    return {"access_token": token}

@router.get("/most_items_sold")
def get_most_items_sold(start_date: date, end_date: date = date.today(), user=Depends(verify_token)):
    return most_sold_items_list.most_sold_items(start_date, end_date)

@router.get("/least_items_sold")
def get_least_items_sold(start_date: date, end_date: date = date.today(), user=Depends(verify_token)):
    return least_sold_items_list.least_items_sold(start_date, end_date)

@router.get("/monthly_data")
def get_monthly_data(year: int, month: int, user=Depends(verify_token)):
    return monthly_data_list.monthly_data(year, month)
