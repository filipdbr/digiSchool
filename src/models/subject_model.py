from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from src.models.base_model import Base


class Subject(Base):
    """
    Represents a subject entity, mapped to the 't_classe' table in the sql database.
    """
    __tablename__ = 't_matiere'

    subject_id = Column("idmatiere", Integer, primary_key=True, autoincrement=True)
    name = Column("nom", String(250), unique=True, nullable=False)

    # Relationships

    # One to many with grades
    grades = relationship("Grade", back_populates="subject")

