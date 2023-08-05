from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID, uuid4


class Airport(BaseModel):
    id: UUID = uuid4()
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    code: str
    latitude: float
    longitude: float
    name: str
    city: str
    country: str
    tz: str
    phone: Optional[str] = None
    email: Optional[str] = None
    url: Optional[HttpUrl] = None
    runway_lenght: int = 0
    elevation: Optional[int] = None
    # ICAO airport code or location indicator is a four-letter code
    # designating aerodromes around the world.
    # Source: https://en.wikipedia.org/wiki/ICAO_airport_code
    icao: str
    direct_flights: int
    carriers: int

    class Config:
        # Pydantic's from_attributes will tell the Pydantic model to read
        # the data even if it is not a dict, but an ORM model (or any other
        # arbitrary object with attributes).
        from_attributes = True
