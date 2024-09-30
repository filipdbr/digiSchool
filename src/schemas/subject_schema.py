from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy import String


class SubjectSchema(BaseModel):
    """
    Represents a subject entity for data validation.

    Attributes:
        subject_id (Optional[int]): Unique identifier for the subject.
        name (Optional[String]): Name of the subject.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    subject_id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True  # Enables using instances of SQLAlchemy models directly