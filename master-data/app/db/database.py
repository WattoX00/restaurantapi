from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./master_data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
