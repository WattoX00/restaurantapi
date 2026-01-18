from abc import ABC, abstractmethod
from schemas.md_schemas import MenuRequest, MenuId

class AddMenuItem(ABC):
    @abstractmethod
    def addItems(self, request: MenuRequest):
        pass

class MenuItemId(ABC):
    @abstractmethod
    def menuItemId(self, id: MenuId):
        pass