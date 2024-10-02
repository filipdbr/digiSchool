from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.base_model import Base

class Trimester(Base):
    """
    Represents a trimester entity, mapped to the 't_trimestre' table in the SQL database.
    """
    __tablename__ = 't_trimestre'

    trimester_id = Column("idtrimestre", Integer, primary_key=True, autoincrement=True)
    name = Column("nom", String(100), unique=True, nullable=False)

    # Relationships
    grades = relationship("Grade", back_populates="trimester")
