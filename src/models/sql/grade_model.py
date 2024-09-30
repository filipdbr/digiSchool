from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.sql.base_model import Base
from src.models.sql.trimester_model import Trimester
from src.models.sql.subject_model import Subject
from src.models.sql.professor_model import Professor


class Grade(Base):
    """
    Represents a grade entity, mapped to the 't_notes' table in the sql database.
    """
    __tablename__ = 't_notes'

    grade_id = Column(Integer, primary_key=True, name = "idnotes")
    student_id = Column(Integer, ForeignKey('t_eleve.id'), name="ideleve")
    subject_id = Column(Integer, ForeignKey('t_matiere.idmatiere'), name="idmatiere")
    class_id = Column(Integer, ForeignKey('t_classe.id'), name="idclasse")
    professor_id = Column(Integer, ForeignKey('t_prof.id'), name="idprof")
    trimester_id = Column(Integer, ForeignKey('t_trimestre.idtrimestre'), name="idtrimestre")
    grade_value = Column(Integer, name="note")
    comment = Column(String(255), default=None, name="avis")
    progress = Column(Float, default=None, name="avancement")
    entry_date = Column(DateTime, default=None, name="date_saisie")

    # Relationships
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    trimester = relationship("Trimester", back_populates="grades")
    professor = relationship("Professor", back_populates="grades")
    student_class = relationship("Class", back_populates="grades")
