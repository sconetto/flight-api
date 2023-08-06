from sqlalchemy import Column, Integer, Float, String, DateTime

from src.data.engine.engine import Base


class Airport(Base):
    __tablename__ = "airport"

    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    code = Column(String, unique=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    name = Column(String)
    city = Column(String)
    country = Column(String)
    tz = Column(String)
    phone = Column(String, default=None)
    email = Column(String, unique=True, default=None)
    url = Column(String, default=None)
    runway_length = Column(Integer)
    elevation = Column(Integer, default=None)
    icao = Column(String, unique=True, index=True)
    direct_flights = Column(Integer)
    carriers = Column(Integer)
