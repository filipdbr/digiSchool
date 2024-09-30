from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base

class Trimester(Base):
    """
    Represents a trimester entity, mapped to the 't_trimestre' table in the database.
    """
    __tablename__ = 't_trimestre'

    id = Column(Integer, primary_key=True, name="idtrimestre")
    name = Column(String(10), name="nom")

    # Relationships

    # One to many with Grades
    grades = relationship("Grade", back_populates="trimester")
