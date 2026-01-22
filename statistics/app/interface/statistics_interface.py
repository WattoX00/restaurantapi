from abc import ABC, abstractmethod
from schemas.statistics_schemas import StarDate, EndDate

# add abs time checking

class CheckTime(ABC):
    def check_time_params(self, start_date: StarDate, end_date: EndDate):
        pass
