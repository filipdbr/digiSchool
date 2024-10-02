from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base_model import Base


class Grade(Base):
    """
    Represents a grade entity, mapped to the 't_notes' table in the sql database.
    """
    __tablename__ = 't_notes'

    grade_id = Column('idnotes', Integer, primary_key=True)
    student_id = Column('ideleve', Integer, ForeignKey('t_eleve.id'))
    subject_id = Column('idmatiere', Integer, ForeignKey('t_matiere.idmatiere'))
    class_id = Column('idclasse', Integer, ForeignKey('t_classe.id'))
    professor_id = Column('idprof', Integer, ForeignKey('t_prof.id'))
    trimester_id = Column('idtrimestre', Integer, ForeignKey('t_trimestre.idtrimestre'))
    grade_value = Column('note', Integer)
    comment = Column('avis', String(255), default=None)
    progress = Column('avancement', Float, default=None)
    date_entered = Column('date_saisie', DateTime, default=None)

    # Relationships
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    trimester = relationship("Trimester", back_populates="grades")
    professor = relationship("Professor", back_populates="grades")
    student_class = relationship("Class", back_populates="grades")
