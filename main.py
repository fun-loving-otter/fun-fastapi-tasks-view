from fastapi import FastAPI

from db import database
from handlers import router

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router, prefix="/api/v1")
