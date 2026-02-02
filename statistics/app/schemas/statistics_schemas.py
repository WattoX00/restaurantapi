from pydantic import BaseModel, conint
from datetime import datetime, date

# add time checking

class StarDate(BaseModel):
    start_date: date

class EndDate(BaseModel):
    end_date: date

class Year(BaseModel):
    year: int

class Month(BaseModel):
    month: conint(ge=0, le=11)


def time_of_day(dt: datetime) -> str:
    h = dt.hour
    if 6 <= h < 11:
        return "morning"
    if 11 <= h < 13:
        return "noon"
    if 13 <= h < 18:
        return "afternoon"
    return "outside_work_hours"

