from .database.database import SessionLocal, engine
from .models import dog

dog.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()