from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MenuItem(Base):
    __tablename__ = "menu_items"
    
    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    ingredients = Column(JSON, nullable=False)
    allergies = Column(JSON, nullable=False)
    availability = Column(Boolean, default=True)