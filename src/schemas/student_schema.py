from pydantic import BaseModel, field_validator, field_serializer
from typing import List, Optional
from datetime import datetime, date

from src.schemas.class_schema import ClassSchema
from src.schemas.grade_schema import GradeSchema

class StudentPatch(BaseModel):
    """
    Represents the schema for partially updating a student entity.

    Attributes:
        last_name (Optional[str]): Last name of the student.
        first_name (Optional[str]): First name of the student.
        date_of_birth (Optional[date]): Birth date of the student.
        address (Optional[str]): Address of the student, optional.
        gender (Optional[str]): Gender of the student.
        student_class (Optional[ClassSchema]): Class the student belongs to, optional.
        grades (Optional[List[GradeSchema]]): List of grades for the student, can be empty or updated.
    """
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    gender: Optional[str] = None
    student_class: Optional[ClassSchema] = None
    grades: Optional[List[GradeSchema]] = None

    @field_serializer('date_of_birth')
    def serialize_date_of_birth(self, value):
        if value:
            return value.strftime('%Y-%m-%d')
        return value

    @field_validator("date_of_birth", mode='before')
    def validate_date_of_birth(cls, value) -> Optional[date]:
        if value is None:
            return value
        if isinstance(value, datetime):
            return value.date()  # datetime to date
        elif isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected format: YYYY-MM-DD.")
        return value

    class Config:
        from_attributes = True

class StudentSchema(StudentPatch):
    """
    Represents a student entity for data validation.

    Attributes:
        student_id (int): Unique identifier for the student.
        last_name (str): Last name of the student.
        first_name (str): First name of the student.
        birth_date (date): Birth date of the student.
        address (Optional[str]): Address of the student, optional.
        gender (str): Gender of the student.
        student_class (Optional[ClassSchema]): Class the student belongs to, optional.
        grades (List[GradeSchema]): List of grades for the student, can be empty.
    """
    student_id: int
    last_name: str
    first_name: str
    date_of_birth: date
    address: Optional[str] = None
    gender: str
    student_class: Optional[ClassSchema] = None
    grades: List[GradeSchema] = []

    @field_serializer('date_of_birth')
    def serialize_date_of_birth(self, value):
        return value.strftime('%Y-%m-%d')

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

class StudentResponse(BaseModel):
    student_id: int
    last_name: str
    first_name: str
    date_of_birth: date
    address: Optional[str] = None
    gender: str
    student_class: Optional[dict] = None

    @field_serializer('student_class')
    def serialize_student_class(self, value):
        if value:
            # convert to a dictionary
            class_obj = ClassSchema(**value) if isinstance(value, dict) else value
            return {
                "class_name": class_obj.name,
                "teacher_last_name": class_obj.professor.last_name,
                "teacher_first_name": class_obj.professor.first_name
            }
        return None

    class Config:
        from_attributes = True

class StudentCreateSchema(BaseModel):
    last_name: str
    first_name: str
    date_of_birth: date
    gender: str
    address: Optional[str] = None

    @field_serializer('date_of_birth')
    def serialize_date_of_birth(self, value):
        return value.strftime('%Y-%m-%d')

    @field_validator("date_of_birth", mode='before')
    def validate_date_of_birth(cls, value) -> date:
        if isinstance(value, datetime):
            return value.date()  # Convert datetime to date
        elif isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected format: YYYY-MM-DD.")
        return value

