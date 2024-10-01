from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy import String


class TrimesterSchema(BaseModel):
    """
    Represents a trimester entity for data validation.

    Attributes:
        trimester_id (Optional[int]): Unique identifier for the trimester.
        name (Optional[str]): Name of the trimester.

    Config:
        orm_mode (bool): Enables compatibility with ORM objects (e.g., SQLAlchemy models).
    """
    trimester_id: Optional[int]
    name: Optional[str]

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly

class TrimesterResponse(BaseModel):
    """
    Represents a trimester entity for the API response, excluding the trimester ID.

    Attributes:
        name (str): Name of the trimester.
    """
    name: str

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly