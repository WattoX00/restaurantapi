from fastapi import APIRouter
from datetime import date
from services.statistics_services import MostSoldItems
router = APIRouter()

most_sold_items_list = MostSoldItems()

@router.get("/most_items_sold")
def get_most_items_sold(start_date: date, end_date: date = date.today()):
    return most_sold_items_list.most_sold_items(start_date, end_date)

@router.get("/least_items_sold")
def get_least_items_sold():
    pass

@router.get("/monthly_data")
def get_monthly_data():
    pass
