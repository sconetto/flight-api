from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_base_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Wolrd!"}
