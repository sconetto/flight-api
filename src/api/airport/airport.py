import json
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from src.models.airport.airport import Airport

# GET - Read
# POST - Create
# PATCH - Update
# DELETE - Delete
# OPTIONS - Show Routes

# Router for the API
ROUTER = APIRouter()


@ROUTER.post("/", response_model=Airport)
async def create_airport(airport: Airport):
    data = json.loads(airport)
    return data


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
async def create_airport(
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
