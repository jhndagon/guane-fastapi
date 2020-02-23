from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.database import Base

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    picture = Column(String)
    create_data = Column(DateTime)
    is_adopted = Column(Boolean)

