from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.sql.base_model import Base

class Trimester(Base):
    """
    Represents a trimester entity, mapped to the 't_trimestre' table in the SQL database.
    """
    __tablename__ = 't_trimestre'

    trimester_id = Column(Integer, primary_key=True, autoincrement=True, name="idtrimestre")
    name = Column(String(100), unique=True, nullable=False, name="nom")

    # Relationships
    grades = relationship("Grade", back_populates="trimester")
