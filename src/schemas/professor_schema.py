from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProfessorResponse(BaseModel):
    """
    Represents a professor entity for the API response. We decided to exclude some data.
    Response is defined as first as it possesses fewer attributes than ProfessorSchema, hence ProfessorSchema.

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
    date_of_birth: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly

class ProfessorSchema(ProfessorResponse):
    """
    Represents a professor entity for data validation.

    Attributes:
        teacher_id (Optional[int]): Unique identifier for the professor used for data validation.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    teacher_id: Optional[int] = None
