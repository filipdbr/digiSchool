from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base

class Student(Base):
    """
    Represents a student entity, mapped to the 't_eleve' table in the database.
    """
    __tablename__ = 't_eleve'  # Table name in our database in MariaDB

    # Columns from db table t_eleve
    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(100), default = None, name = "nom")
    first_name = Column(String(100), default = None, nullable = True, name = "prenom")
    birth_date = Column(DateTime, default = None, name = "date_naissance")
    address = Column(String(250), default = None, nullable = True, name = "adresse")
    sex = Column(Enum('HOMME', 'FEMME'), default = None, name = "sex")
    class_id = Column(Integer, ForeignKey("t_classe.id"), nullalble = True, name = "classe") # column containing foreign key of t_classe table

    # Relations

    # Many to one with class
    student_class = relationship("Class", back_populates="students")
    # One to many with grades
    grades = relationship("Grade", back_populates="student")



