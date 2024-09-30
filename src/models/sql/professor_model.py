from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base


class Professor(Base):
    """
    Represents a professor entity, mapped to the 't_prof' table in the database.
    """
    __tablename__ = 't_prof'

    # Columns from db table t_prof
    prof_id = Column(Integer, primary_key=True, name = "id")
    last_name = Column(String(100), nullable=False, default=None, name = "nom")
    first_name = Column(String(100), nullable=True, default=None, name = "prenom")
    birth_date = Column(DateTime, nullable = False, default=None, name="date_naissance")
    address = Column(String(250), default=None, nullable=True, name="adresse")
    gender = Column(Enum('HOMME', 'FEMME'), default=None, name="sexe")

    # Relations

    # one to many with class
    classes = relationship("Class", back_populates="professor")

    # one to many
    grades = relationship("Grade", back_populates="professor")
