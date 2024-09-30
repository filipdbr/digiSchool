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
    prof_id = Optional[int]
    last_name = Optional[str]
    first_name = Optional[str]
    birth_date = Optional[datetime]
    address = Optional[str]
    gender = Optional[str]

    class Config:
        orm_mode = True  # Enables using instances of SQLAlchemy models directly