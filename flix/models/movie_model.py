from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    movie = Column(String, nullable=False)
    description = Column(String, nullable=False)
    embedding = Column(Vector(1024), nullable=False)
