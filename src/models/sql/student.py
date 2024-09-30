from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from src.models.sql.base_model import Base

class Student(Base):
    """
    Represents a student entity, mapped to the 't_eleve' table in the database.
    """
    __tablename__ = 't_eleve'  # Table name in our database in MariaDB

    # Columns from our MariaDB table t_eleve
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), default = None)
    prenom = Column(String(100), default = None, nullable = True)
    date_naissance = Column(DateTime, default = None)
    adresse = Column(String(250), default = None, nullable = True)
    sexe = Column(Enum('HOMME', 'FEMME'), default = None)
    classe_id = Column(Integer, ForeignKey("t_classe.id"), nullalble = True) # column containing foreign key of t_classe table

    # Relationship many to one
    classe = relationship("Classe", back_populates="eleves")



