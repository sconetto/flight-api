import json
from fastapi.testclient import TestClient
from pytest import fixture
from src.main import app
from src.data.engine.engine import SessionLocal
from src.data.schema.airport.airport import Airport

URL = "/v1/airport/"

EXAMPLE_PAYLOAD = """
{
  "code": "FRA",
  "latitude": "50.0483",
  "longitude": "8.57041",
  "name": "Frankfurt International Airport",
  "city": "Frankfurt",
  "state": "Hesse",
  "country": "Germany",
  "woeid": "22981759",
  "tz": "Europe/Berlin",
  "phone": "+49 69 690 0",
  "type": "Airports",
  "email": "",
  "url": "http://www.airportcity-frankfurt.de/",
  "runway_length": "13123",
  "elevation": "364",
  "icao": "EDDF",
  "direct_flights": "337",
  "carriers": "131"
}
"""

# Payload with missing code
# Correct code: LHR
WRONG_PAYLOAD = """
{
  "latitude": "51.4703",
  "longitude": "-0.45342",
  "name": "London Heathrow Airport",
  "city": "Hounslow",
  "state": "England",
  "country": "United Kingdom",
  "woeid": "23382429",
  "tz": "Europe/London",
  "phone": "+44 (0)8700 000698",
  "type": "Airports",
  "email": "",
  "url": "http://www.heathrowairport.com/",
  "runway_length": "12802",
  "elevation": "80",
  "icao": "EGLL",
  "direct_flights": "227",
  "carriers": "105"
}
"""
FIELD_MESSAGE = "Field required"
DETAIL_TYPE = "missing"
MISSING_FIELD = "code"

client = TestClient(app)


@fixture
def clean_database():
    """
    Initialize a new session locally and delete test created airport
    """
    db = SessionLocal()
    # TODO: Newer versions create a test database
    db.query(Airport).filter(Airport.code == "FRA").delete()
    db.commit()
    return


def test_create_airport_successful(clean_database):
    payload = json.loads(EXAMPLE_PAYLOAD)
    response = client.post(URL, json=payload)
    data = response.json()
    assert response.status_code == 200
    for key, value in payload.items():
        # don't assert keys that are cleaned to none
        # or mapped to the model
        if key in data.keys() and value:
            assert value == str(data.get(key))


def test_create_airport_unsuccessful():
    payload = json.loads(WRONG_PAYLOAD)
    response = client.post(URL, json=payload)
    data = response.json()
    assert response.status_code == 422
    assert data.get("detail")[0].get("msg") == FIELD_MESSAGE
    assert data.get("detail")[0].get("type") == DETAIL_TYPE
    assert MISSING_FIELD in data.get("detail")[0].get("loc")
