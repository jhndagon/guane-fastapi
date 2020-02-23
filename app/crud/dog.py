from sqlalchemy.orm import Session

from app.models import dog as dog_model
from app.schemas import dog as dog_schema

def get_dogs(db: Session, dog_name: str):
    """
    Get all dogs from database
    """
    return db.query(dog_model.Dog).filter(dog_model.Dog.name == dog_name).first()


def get_adopted_dogs(db: Session, dog_adopted: bool = True):
    """
    Get all adopted dogs from database
    """
    return db.query(dog_model.Dog).filter(dog_model.Dog.is_adopted==dog_adopted).all()


def create_dog(db: Session, dog: dog_schema.DogCreate):
    """
    Create a new dog in database
    """
    dog = dog_model.Dog(name=dog.name, is_adopted=dog.is_adopted, picture=dog.picture, create_data=dog.create_data)
    db.add(dog)
    db.commit()
    db.refresh(dog)
    return dog


def update_dog(db: Session, dog_name: str, dog: dog_model.Dog):
    """
    Update information of a dof
    """
    dog_database = db.query(dog_model.Dog).filter(dog_model.Dog.name == dog_name).first()
    dog_database.is_adopted = dog.is_adopted if dog.is_adopted else dog_database.is_adopted
    dog_database.picture = dog.picture if dog.picture else dog_database.picture
    db.merge(dog_database)
    db.commit()
    db.refresh(dog_database)
    return dog_database


def delete_dog(db: Session, dog_name:str):
    try:
        dog = db.query(dog_model.Dog).filter(dog_model.Dog.name == dog_name).first()
        db.delete(dog)
        db.commit()
        return dog
    except:
        return None