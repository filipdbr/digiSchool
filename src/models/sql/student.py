from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey

from src.models.base_model import Base

# todo add relations

class Student(Base):
    """
    Represents a student entity, mapped to the 't_eleve' table in the database.
    """
    __tablename__ = 't_eleve'  # Table name in our database in MariaDB

    # Columns from our MariaDB table t_eleve
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), default = None)
    prenom = Column(String(100), default = None)
    date_naissance = Column(DateTime, default = None)
    adresse = Column(String(250), default = None)
    sexe = Column(Enum('HOMME', 'FEMME'), default = None)

    # relations

