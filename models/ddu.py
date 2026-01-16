from sqlalchemy import Column, Integer, String
from app.db.base import Base

class DDU(Base):
    __tablename__ = "ddus"

    id = Column(Integer, primary_key=True)
    zip_code = Column(String)
    ddu_code = Column(String)
    households = Column(Integer)
    scf_code = Column(String)
