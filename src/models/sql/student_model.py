from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base

class Student(Base):
    """
    Represents a student entity, mapped to the 't_eleve' table in the database.
    """
    __tablename__ = 't_eleve'  # Table name in our database in MariaDB

    # Columns from db table t_eleve
    student_id = Column('id', Integer, primary_key=True)
    last_name = Column('nom', String(100), nullable=False, default=None)
    first_name = Column('prenom', String(100), nullable=True, default=None)
    birth_date = Column('date_naissance', DateTime, nullable=False, default=None)
    address = Column('adresse', String(250), default=None, nullable=True)
    gender = Column('sexe', String(10), default=None)
    class_id = Column('classe', Integer, ForeignKey('t_classe.id'))

    # Relations

    # Many to one with class
    student_class = relationship("Class", back_populates="students")
    # One to many with grades
    grades = relationship("Grade", back_populates="student")  # Ensure this is properly imported and defined
