from fastapi import FastAPI, Request
from dotenv import load_dotenv
from routers import scrapResult
from contextlib import asynccontextmanager
from typing import Dict
from model import MongoDB
from model.ResponseType import ChartResponse, SexInfo, PartyInfo, AgeInfo


@asynccontextmanager
async def initMongo(app: FastAPI):
    MongoDB.MongoDB().connect()
    yield
    MongoDB.MongoDB().close()

new = ChartResponse[SexInfo]

app = FastAPI(lifespan=initMongo, responses={404: {"description": "Not found"}})


app.include_router(scrapResult.router)
