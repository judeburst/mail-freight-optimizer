from sqlalchemy import Column, Integer, Date, ForeignKey
from app.db.base import Base

class Drop(Base):
    __tablename__ = "drops"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    drop_number = Column(Integer, nullable=False)
    start_day = Column(Integer, nullable=False)
    end_day = Column(Integer, nullable=False)
    in_home_date = Column(Date, nullable=False)
