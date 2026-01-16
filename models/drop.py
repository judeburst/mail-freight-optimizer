from sqlalchemy import Column, Integer, ForeignKey, Date
from app.db.base import Base

class Drop(Base):
    __tablename__ = "drops"

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    drop_number = Column(Integer)
    in_home_date = Column(Date)
    start_day = Column(Integer)
    end_day = Column(Integer)
