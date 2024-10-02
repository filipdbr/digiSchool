from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime, date


class ProfessorSchema(BaseModel):
    """
    Represents a professor entity for the API response. We decided to exclude some data.
    Response is defined as first as it possesses fewer attributes than ProfessorSchema, hence ProfessorSchema.

    Attributes:
        last_name (str): Last name of the professor.
        first_name (str): First name of the professor.
        address(str) Address of the professor.
        gender(str) Gender of the professor.
    """
    teacher_id: int
    last_name: str
    first_name: str
    address: str
    gender: str
    date_of_birth: Optional[datetime] = None

    # Validator for formatting last_name to uppercase
    @field_validator("last_name", mode='before')
    def format_last_name(cls, value: str) -> str:
        return value.strip().upper() if value else value

    # Validator for formatting first_name to capitalize
    @field_validator("first_name", mode='before')
    def format_first_name(cls, value: str) -> str:
        return value.strip().capitalize() if value else value

    # Validator for formatting address to capitalize
    @field_validator("address", mode='before')
    def format_address(cls, value: str) -> str:
        return value.strip().capitalize() if value else value

    # Validator for formatting gender to uppercase
    @field_validator("gender", mode='before')
    def format_gender(cls, value: str) -> str:
        return value.strip().upper() if value else value

    # Validator for casting date_of_birth to a date object if possible
    @field_validator("date_of_birth", mode='before')
    def cast_date_of_birth(cls, value) -> Optional[date]:
        if isinstance(value, datetime):
            return value.date()
        elif isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected format: YYYY-MM-DD.")
        return value

    class Config:
        from_attributes = True  # Enables using instances of SQLAlchemy models directly

class ProfessorResponse(ProfessorSchema):
    """
    Represents a professor entity for response.

    Informing user of prof classes in the response as it's interesting for the user.

    The same as Professor
    """

    classes: List[str] = []

    pass
