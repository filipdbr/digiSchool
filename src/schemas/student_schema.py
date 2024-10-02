from pydantic import BaseModel, field_validator, field_serializer
from typing import List, Optional
from datetime import datetime, date

from src.schemas.class_schema import ClassSchema
from src.schemas.grade_schema import GradeSchema, GradeResponse

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
    date_of_birth: datetime
    address: Optional[str]
    gender: str
    student_class: Optional[ClassSchema] = None
    grades: List[GradeSchema] = []

    @field_serializer('date_of_birth')
    def serialize_date_of_birth(self, value):
        return value.strftime('%Y-%m-%d')

    # Validator dla date_of_birth, aby upewnić się, że data jest odpowiednio przekształcona
    @field_validator("date_of_birth", mode='before')
    def validate_date_of_birth(cls, value) -> date:
        if isinstance(value, datetime):
            return value.date()  # datetime to date
        elif isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected format: YYYY-MM-DD.")
        return value

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly

class StudentResponse(StudentSchema):
    pass

class StudentAPI(StudentSchema):
    date_of_birth: date
