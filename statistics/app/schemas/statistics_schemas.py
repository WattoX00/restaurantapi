from pydantic import BaseModel, Field, conint, field_validator
from datetime import date

# add time checking

class StarDate(BaseModel):
    start_date: date

class EndDate(BaseModel):
    end_date: date

COMPANY_START_YEAR = 2018  # hardcode for now

class Year(BaseModel):
    year: int = Field(ge=COMPANY_START_YEAR)

    @field_validator("year")
    @classmethod
    def not_in_future(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError("year cannot be in the future")
        return v

class Month(BaseModel):
    month: conint(ge=0, le=11)
