"""
This module defines Pydantic schemas for data validation in the application.

Schemas represent entities such as professors, students, classes, subjects, trimesters, and grades.
Each schema also uses aliases to map attributes to their respective names in the database,
allowing for smooth integration between different naming conventions (e.g., from SQL to NoSQL).

Classes:
- ProfessorSchema: Represents a professor entity with attributes such as name, gender, and address.
- ClassSchema: Represents a class entity, including the class's professor.
- SubjectSchema: Represents a subject entity.
- TrimesterSchema: Represents a trimester entity.
- GradeSchema: Represents a grade entity, including information about subject, trimester, and student progress.
- StudentSchema: Represents a student entity, including information about class and grades.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ProfessorSchema(BaseModel):
    """
    Schema for a professor entity.
    Includes details such as teacher ID, name, birth date, address, and gender.
    """
    professor_id: Optional[int] = Field(None, alias="prof_id")
    last_name: Optional[str] = Field(None, alias="nom")
    first_name: Optional[str] = Field(None, alias="prenom")
    date_of_birth: Optional[datetime] = Field(None, alias="date_naissance")
    address: Optional[str] = Field(None, alias="adresse")
    gender: Optional[str] = Field(None, alias="sexe")

    class Config:
        allow_population_by_field_name = True

class ClassSchema(BaseModel):
    """
    Schema for a class entity.
    Contains class ID, class name, and optional information about the professor teaching the class.
    """
    class_id: Optional[int] = Field(None, alias="class_id")
    name: Optional[str] = Field(None, alias="nom")
    professor: Optional[ProfessorSchema] = None

    class Config:
        allow_population_by_field_name = True

class SubjectSchema(BaseModel):
    """
    Schema for a subject entity.
    Contains subject ID and subject name.
    """
    subject_id: Optional[int] = Field(None, alias="matiere_id")
    name: Optional[str] = Field(None, alias="nom")

    class Config:
        allow_population_by_field_name = True

class TrimesterSchema(BaseModel):
    """
    Schema for a trimester entity.
    Contains trimester ID and trimester name.
    """
    trimester_id: Optional[int] = Field(None, alias="trimestre_id")
    name: Optional[str] = Field(None, alias="nom")

    class Config:
        allow_population_by_field_name = True

class GradeSchema(BaseModel):
    """
    Schema for a grade entity.
    Includes grade ID, subject details, grade value, entry date, trimester, comment, and progress.
    """
    grade_id: Optional[int] = Field(None, alias="note_id")
    subject: Optional[SubjectSchema] = None
    grade_value: Optional[int] = Field(None, alias="note")
    date_entered: Optional[datetime] = Field(None, alias="date_saisie")
    trimester: Optional[TrimesterSchema] = None
    comment: Optional[str] = Field(None, alias="avis")
    progress: Optional[float] = Field(None, alias="avancement")

    class Config:
        allow_population_by_field_name = True

class StudentSchema(BaseModel):
    """
    Schema for a student entity.
    Contains student ID, name, birth date, address, gender, class details, and a list of grades.
    """
    student_id: int = Field(..., alias="_id")
    last_name: str = Field(..., alias="nom")
    first_name: str = Field(..., alias="prenom")
    date_of_birth: datetime = Field(..., alias="date_naissance")
    address: Optional[str] = Field(None, alias="adresse")
    gender: str = Field(..., alias="sexe")
    student_class: Optional[ClassSchema] = Field(None, alias="classe")
    notes: List[GradeSchema] = []

    class Config:
        allow_population_by_field_name = True
