from sqlalchemy import Column, Integer, String
from .database import Base

class get_kbo_data(Base):
    __tablename__ = "kbo_player"

    kbo_id = Column(String(10),primary_key=True)
    name = Column(String(30))
    team = Column(String(10))