from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from src.schemas.class_schema import ClassSchema
from src.schemas.grade_schema import GradeSchema


class StudentSchema(BaseModel):
    """
    Represents a student entity for data validation.

    Attributes:
        student_id (int): Unique identifier for the student.
        last_name (str): Last name of the student.
        first_name (str): First name of the student.
        birth_date (datetime): Birth date of the student.
        address (Optional[str]): Address of the student, optional.
        gender (str): Gender of the student.
        student_class (Optional[ClassSchema]): Class the student belongs to, optional.
        grades (List[GradeSchema]): List of grades for the student, can be empty.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    student_id: int
    last_name: str
    first_name: str
    birth_date: datetime
    address: Optional[str]
    gender: str
    student_class: Optional[ClassSchema] = None
    grades: List[GradeSchema] = []

    class Config:
        orm_mode = True  # Enables using instances of SQLAlchemy models directly