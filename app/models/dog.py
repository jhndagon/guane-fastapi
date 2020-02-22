from pydantic import BaseModel
from datetime import datetime

class Dog(BaseModel):
    name: str
    picture: str
    create_data: datetime = datetime.now()
    is_adopted: bool