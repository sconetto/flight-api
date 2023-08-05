from fastapi import FastAPI

from src.api.airport.airport import ROUTER as AIRPORT
from src.utils.utils import get_variable
from src.data.engine.engine import engine, SessionLocal
from src.data.schema.airport import airport

import uvicorn

HOST = get_variable("HOST", str) or "127.0.0.1"
PORT = get_variable("PORT", int) or 8080
VERSION = get_variable("VERSION", str) or "0.0.0"

app = FastAPI(
    title="Flight API 🛩️",
    description="A lightweight generic API for flight related information",
    version=VERSION,
)

app.include_router(AIRPORT, prefix="/v1/airport", tags=["Airport"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"Hello": "Wolrd!"}


if __name__ == "__main__":
    airport.Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
