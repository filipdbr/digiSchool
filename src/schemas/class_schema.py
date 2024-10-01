from pydantic import BaseModel
from typing import List, Optional
from src.schemas.professor_schema import ProfessorSchema


class ClassSchema(BaseModel):
    """
    Represents a class entity for data validation.

    Attributes:
        class_id (Optional[int]): Unique identifier for the class.
        name (Optional[str]): The name of the class.
        professor (Optional[ProfessorSchema]): The professor associated with the class.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    class_id: Optional[int]
    name: Optional[str]
    professor: Optional[ProfessorSchema]

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly