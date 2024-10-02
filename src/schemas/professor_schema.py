from pydantic import BaseModel, field_validator, field_serializer, validator
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

    @field_serializer('date_of_birth')
    def serialize_date_of_birth(self, value):
        return value.strftime('%Y-%m-%d')

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

class ProfessorAPI(ProfessorSchema):
    """
    Schema for user entry in API. Changes the format of date of birth.
    """
    date_of_birth: Optional[date] = None

class ProfessorUpdateSchema(BaseModel):
    """
    Schema for updating a professor's details. Excludes 'teacher_id' and 'classes'.
    """
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None  # Accept date_of_birth as a string

    # Validators for formatting fields using field_validator
    @field_validator("last_name", mode='before')
    def format_last_name(cls, value):
        return value.strip().upper() if value else value

    @field_validator("first_name", mode='before')
    def format_first_name(cls, value):
        return value.strip().capitalize() if value else value

    @field_validator("address", mode='before')
    def format_address(cls, value):
        return value.strip().capitalize() if value else value

    @field_validator("gender", mode='before')
    def format_gender(cls, value):
        return value.strip().upper() if value else value

    @field_validator('date_of_birth', mode='before')
    def validate_date_of_birth(cls, value):
        if value:
            try:
                # Validate the date format
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValueError("date_of_birth must be in YYYY-MM-DD format")
        return value

    class Config:
        from_attributes = True

