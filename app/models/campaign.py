from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    dealer_name = Column(String, nullable=False)
    sale_length_days = Column(Integer, nullable=False)
