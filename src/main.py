import socket
import sys

from fastapi import FastAPI, Request

app = FastAPI()

hostname = socket.gethostname()

version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.get("/")
async def read_root():
    return {
        "name": "my-app",
        "host": hostname,
        "version": f"Hello world! From FastAPI running on Uvicorn. Using Python {version}"
    }


@app.get("/ping")
async def read_ping():
    return {"ping": "pong"}


@app.post("/echo")
async def echo(request: Request):
    return await request.json()
