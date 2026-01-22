from pydantic import BaseModel
from datetime import date

# add time checking

class StarDate(BaseModel):
    start_date: date

class EndDate(BaseModel):
    end_date: date
