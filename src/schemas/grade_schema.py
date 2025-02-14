from pydantic import BaseModel, field_serializer, field_validator
from typing import List, Optional
from datetime import datetime, date
from src.schemas.subject_schema import SubjectSchema
from src.schemas.trimester_schema import TrimesterSchema


class GradeSchema(BaseModel):
    """
    Represents a grade entity for data validation.

    Attributes:
        grade_id (Optional[int]): Unique identifier for the grade.
        subject (Optional[SubjectSchema]): The subject related to the grade.
        grade_value (Optional[int]): The value of the grade.
        date_entered (Optional[datetime]): The date when the grade was entered.
        trimester (Optional[TrimesterSchema]): The trimester during which the grade was given.
        comment (Optional[str]): Any comments related to the grade.
        progress (Optional[float]): The progress value associated with the grade.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    grade_id: Optional[int]
    subject: Optional[SubjectSchema]
    grade_value: Optional[int]
    date_entered: Optional[datetime]
    trimester: Optional[TrimesterSchema]
    comment: Optional[str]
    progress: Optional[float]

    @field_serializer('date_entered')
    def serialize_date_entered(self, value):
        return value.strftime('%Y-%m-%d')

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly

class GradeResponse(GradeSchema):
    pass

class GradeAPI(GradeSchema):
    date_entered: Optional[date]