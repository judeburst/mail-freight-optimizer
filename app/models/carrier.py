from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Carrier(Base):
    __tablename__ = "carriers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
