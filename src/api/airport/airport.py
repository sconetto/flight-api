from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.data.engine.engine import get_db
from src.data.schema.airport.crud import (
    get_airport_by_code,
    get_airport_by_icao,
    create_airport as db_create_airport,
)
from src.models.airport.airport import Airport

# GET - Read
# POST - Create
# PATCH - Update
# DELETE - Delete
# OPTIONS - Show Routes

# Router for the API
ROUTER = APIRouter()


@ROUTER.post("/", response_model=Airport)
async def create_airport(airport: Airport, db: Session = Depends(get_db)):
    if get_airport_by_code(db, airport.code):
        raise HTTPException(
            status_code=400,
            detail=f"Airport with Code {airport.code} already exists!"
        )

    if get_airport_by_icao(db, airport.icao):
        raise HTTPException(
            status_code=400,
            detail=f"Airport with ICAO code {airport.icao} already exists!",
        )

    try:
        db_create_airport(db, airport)
        return airport
    except Exception as err:
        raise HTTPException(
            status_code=500,
            detail=f"Error while creating airport. Traceback: {err}",
        )


@ROUTER.options("/")
async def describe_route():
    return {
        "GET": "/v1/airport/{identifier}",
        "DELETE": "/v1/airport/{identifier}",
        "PATCH": "/v1/airport/{identifier}",
        "POST": "/v1/airport/",
    }


# TODO: Work on missing API routes operations when time available


@ROUTER.get("/{identifier}", response_model=Airport)
async def get_airport(
    identifier: str,
):
    raise NotImplementedError


@ROUTER.delete("/{identifier}", response_model=Airport)
async def detelet_airport(
    identifier: str,
):
    raise NotImplementedError


@ROUTER.post("/{identifier}", response_model=Airport)
async def update_airport(
    identifier: str,
):
    raise NotImplementedError
