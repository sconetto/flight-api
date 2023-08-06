from datetime import datetime
from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator
from typing import Optional
from uuid import UUID, uuid4


class Airport(BaseModel):
    # Pydantic's from_attributes will tell the Pydantic model to read
    # the data even if it is not a dict, but an ORM model (or any other
    # arbitrary object with attributes).
    model_config = ConfigDict(from_attributes=True)
    id: UUID = uuid4()
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    code: str
    latitude: float
    longitude: float
    name: str
    city: str
    state: str
    country: str
    tz: str
    phone: Optional[str] = None
    email: Optional[str] = None
    url: Optional[HttpUrl] = None
    runway_length: int
    elevation: Optional[int] = None
    # ICAO airport code or location indicator is a four-letter code
    # designating aerodromes around the world.
    # Source: https://en.wikipedia.org/wiki/ICAO_airport_code
    icao: str
    direct_flights: int
    carriers: int

    @field_validator("phone")
    @classmethod
    def validate_empty_phones(cls, value):
        if not value:
            return None
        return value

    @field_validator("email")
    @classmethod
    def validate_empty_emails(cls, value):
        if not value:
            return None
        return value

    @field_validator("url")
    @classmethod
    def validate_empty_urls(cls, value):
        if not value:
            return None
        return value

    @field_validator("elevation")
    @classmethod
    def validate_elevation(cls, value):
        if not value:
            return None
        elif value and isinstance(value, str):
            return int(value)
        return value
