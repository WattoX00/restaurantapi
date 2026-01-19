from fastapi import APIRouter
from datetime import date

router = APIRouter()

@router.get("/most_items_sold")
def get_most_items_sold(start_date: date, end_date: date):
    pass