from sqlalchemy.orm import Session

from src.data.schema.airport import airport as schema


def get_airport(db: Session, idx: str):
    return db.query(schema.Airport).filter(schema.Airport.id == idx).first()


def get_airport_by_code(db: Session, code: str):
    return db.query(schema.Airport).filter(schema.Airport.code == code).first()


def get_airport_by_icao(db: Session, icao: str):
    return db.query(schema.Airport).filter(schema.Airport.icao == icao).first()


def get_airports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schema.Airport).offset(skip).limit(limit).all()


def create_airport(db: Session, airport: schema.Airport):
    record = schema.Airport(
        id=str(airport.id),
        created_at=airport.created_at,
        updated_at=airport.updated_at,
        code=airport.code,
        latitude=airport.latitude,
        longitude=airport.longitude,
        name=airport.name,
        city=airport.city,
        country=airport.country,
        tz=airport.tz,
        phone=airport.phone,
        email=airport.email,
        url=str(airport.url),
        runway_length=airport.runway_length,
        elevation=airport.elevation,
        icao=airport.icao,
        direct_flights=airport.direct_flights,
        carriers=airport.carriers,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


# TODO: Work on missing CRUD operations when time available


def update_airport(db: Session, airport: schema.Airport):
    raise NotImplementedError


def delete_airport(db: Session, idx: str):
    raise NotImplementedError


def delete_airport_by_code(db: Session, code: str):
    raise NotImplementedError


def delete_airport_by_icao(db: Session, icao: str):
    raise NotImplementedError
