from fastapi import FastAPI

from .api import dogs

app = FastAPI()

app.include_router(dogs.router, prefix="/api/dogs")
