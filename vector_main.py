# This is a version of the main.py file found in ../../../server/main.py for testing the plugin locally.
# Use the command `poetry run dev` to run this.
import uvicorn
from fastapi import FastAPI, HTTPException, Body
from loguru import logger

from models.api import (
    QueryRequest,
    QueryResponse,
)
from contextlib import asynccontextmanager
from datastore.factory import get_datastore

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    global datastore
    datastore = await get_datastore()
    yield


app = FastAPI(lifespan=lifespan)

PORT = 3333

origins = [
    f"http://localhost:{PORT}",
    "https://chat.openai.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query", response_model=QueryResponse)
async def query_main(request: QueryRequest = Body(...)):
    try:
        results = await datastore.query(
            request.queries,
        )
        return QueryResponse(results=results)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal Service Error")


def start():
    uvicorn.run("local_server.main:app", host="localhost", port=PORT, reload=True)
