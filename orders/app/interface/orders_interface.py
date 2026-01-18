from abc import ABC, abstractmethod
from schemas.orders_schemas import NewOrderElement

class NewOrder(ABC):
    
    @abstractmethod
    def add_new_order(self, orderList: NewOrderElement):
        pass