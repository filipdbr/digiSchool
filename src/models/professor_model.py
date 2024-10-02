from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from src.models.base_model import Base


class Professor(Base):
    """
    Represents a professor entity, mapped to the 't_prof' table in the database.
    """
    __tablename__ = 't_prof'

    # Columns from db table t_prof
    teacher_id = Column('id', Integer, primary_key=True)
    last_name = Column('nom', String(100), nullable=False, default=None)
    first_name = Column('prenom', String(100), nullable=True, default=None)
    birth_date = Column('date_naissance', DateTime, nullable=False, default=None)
    address = Column('adresse', String(250), default=None, nullable=True)
    gender = Column('sexe', Enum('HOMME', 'FEMME'), default=None)

    # Relations

    # one to many with class
    classes = relationship("Class", back_populates="professor")

    # one to many
    grades = relationship("Grade", back_populates="professor")
