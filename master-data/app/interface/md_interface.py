from abc import ABC, abstractmethod
from schemas.md_schemas import MenuRequest

class AddMenuItem(ABC):
    @abstractmethod
    def addItems(self, request: MenuRequest):
        pass