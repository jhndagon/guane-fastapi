from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from sqlalchemy.orm import Session

from app.crud import dog as dog_crud
import app.models.dog as dog_models
import app.schemas.dog as dog_schema

from app.services.dog_picture import get_dog_picture_url

from app.config import get_db

router = APIRouter()


@router.get("/is_adopted", status_code=200)
def read_adopted_dogs(db: Session=Depends(get_db)):
    dogs = dog_crud.get_adopted_dogs(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(dogs))


@router.get("/{name}", status_code=200)
def read_dog(name: str, db: Session=Depends(get_db)):
    dogs = dog_crud.get_dogs(db, name)
    return JSONResponse(status_code=200, content=jsonable_encoder(dogs))


@router.post(
    "/{name}",
    response_model=dog_schema.DogBase
    )
def insert_dog(name: str, db: Session=Depends(get_db)):
    """
    Create a new dog registry
    """
    url = get_dog_picture_url()
    if url: 
        dog = dog_schema.DogBase(name = name, is_adopted=False, picture= url)
        db_dog = dog_crud.create_dog(db, dog)
        return JSONResponse(status_code=201, content=jsonable_encoder(db_dog))
    return JSONResponse(status_code=204, content="")


@router.put(
        "/{name}",
        response_model=dog_schema.DogBase
    )
def update_dog(
        name: str, 
        dog: dog_schema.DogBase = Body(..., example={"is_adopted": True}), 
        db: Session = Depends(get_db)
    ):
    dog_database = dog_crud.update_dog(db, name, dog)
    return JSONResponse(status_code=200, content=jsonable_encoder(dog_database))


@router.delete("/{name}", response_model=dog_schema.DogBase)
def delete_dog(name: str, db:Session=Depends(get_db)):
    dog = dog_crud.delete_dog(db, name)
    return dog