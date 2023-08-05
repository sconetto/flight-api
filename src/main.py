from fastapi import FastAPI
from src.utils.utils import get_variable

import uvicorn

HOST = get_variable("HOST", str) or "127.0.0.1"
PORT = get_variable("PORT", int) or 8080
VERSION = get_variable("VERSION", str) or "0.0.0"

app = FastAPI(
    title="Flight API 🛩️",
    description="A lightweight generic API for flight related information",
    version=VERSION,
)


@app.get("/")
async def root():
    return {"Hello": "Wolrd!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
