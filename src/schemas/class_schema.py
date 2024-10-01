from pydantic import BaseModel
from typing import Optional
from src.schemas.professor_schema import ProfessorSchema


# todo here I don't have to add Optional because I've already defined it in scheme Student
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

class ClassResponse(BaseModel):
    """
    Represents a class entity for the API response, excluding the class ID.

    Attributes:
        name (str): The name of the class.
        professor (Optional[ProfessorSchema]): The professor associated with the class.
    """
    name: str
    professor: Optional[ProfessorSchema]

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly