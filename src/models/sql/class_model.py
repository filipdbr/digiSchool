from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base


class Class(Base):
    """
    Represents a class entity, mapped to the 't_classe' table in the sql database.
    """
    __tablename__ = 't_classe'

    # Columns from db table t_classe
    class_id = Column(Integer, primary_key=True, autoincrement=True, name = "id")
    name = Column(String(100), default = None,nullable = True, name = "nom")
    professor_id = Column(Integer, ForeignKey('t_prof.id'), name="prof")

    # Relations

    # one to many with students
    students = relationship("Student", back_populates="student_class")

    # many to one with prof
    professor = relationship("Professor", back_populates="classes")

    # one to many with grades
    grades = relationship("Grade", back_populates="student_class")