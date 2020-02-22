from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.models.dog import Dog
from app.services.dog_picture import get_dog_picture_url

router = APIRouter()

@router.get("/{name}", status_code=200)
def read_dod(name: str):
    return {"dog": "name "+ name}


@router.get("/is_adopted", status_code=200)
def read_adopted_dogs():
    return {"dogs": "adopted dogs"}


@router.post(
    "/{name}",
    response_model=Dog
    )
def insert_dog(name: str):
    """
    Create a new dog registry
    """
    url = get_dog_picture_url()
    if url: 
        dog = Dog(name = name, is_adopted=False, picture= url)
        return JSONResponse(status_code=201, content=jsonable_encoder(dog))
    return JSONResponse(status_code=204, content="")



@router.put("/{name}")
def update_dog(name: str):
    return {"dog": "update a dog"}


@router.delete("/{name}")
def delete_dog(name: str):
    return {"dog": "delete a dog"}