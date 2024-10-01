from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProfessorSchema(BaseModel):
    """
    Represents a professor entity for data validation.

    Attributes:
        prof_id (Optional[int]): Unique identifier for the professor.
        last_name (Optional[str]): Last name of the professor.
        first_name (Optional[str]): First name of the professor.
        birth_date (Optional[datetime]): Birth date of the professor.
        address (Optional[str]): Address of the professor.
        gender (Optional[str]): Gender of the professor.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    teacher_id: Optional[int] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    address: Optional[str] = None
    gender: Optional[str] = None

    class Config:
        from_attributes = True # Enables using instances of SQLAlchemy models directly


class ProfessorResponse(BaseModel):
    """
    Represents a professor entity for the API response. We decided to exclude some data.

    Attributes:
        last_name (str): Last name of the professor.
        first_name (str): First name of the professor.
        address(str) Address of the professor.
        gender(str) Gender of the professor.
    """
    last_name: str
    first_name: str
    address: str
    gender: str

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly
