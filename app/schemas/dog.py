from pydantic import BaseModel
from datetime import datetime


class DogBase(BaseModel):
    name: str = None
    picture: str = None
    create_data: datetime = datetime.now()
    is_adopted: bool


class DogCreate(DogBase):
    pass


class Dog(DogBase):
    id: int

    class Config:
        orm_mode = True
