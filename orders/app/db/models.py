from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Orders(Base):
    __tablename__ = "menu_items"
    
    id = Column(Integer, primary_key=True, index=True)
    food_names = Column(JSON, nullable=False)
    table_number = Column(Integer, nullable=False)
    description = Column(JSON, nullable=True)
    time = Column(DateTime, nullable=False)
    finished = Column(Boolean, default=False)
