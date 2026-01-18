from sqlalchemy import Column, Integer, String
from app.db.base import Base

class DDU(Base):
    __tablename__ = "ddus"

    id = Column(Integer, primary_key=True)
    zip_code = Column(String, nullable=False)
    ddu_code = Column(String, nullable=False)
    scf_code = Column(String, nullable=False)
    households = Column(Integer, nullable=False)
