from fastapi import APIRouter
from src.controllers.professor_controller import get_all_professors
from src.schemas.professor_schema import ProfessorResponse
from typing import List

router = APIRouter()

@router.get(
    "/professors",
    summary="Retrieve the list of professors",
    response_model=List[ProfessorResponse]
)
def get_professors(skip: int = 0, limit: int = 10) -> List[ProfessorResponse]:
    """
    Retrieves a list of professors.

    Args:
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return.

    Returns:
        List[ProfessorResponse]: A list of professors.
    """
    # Call the controller function with pagination parameters
    return get_all_professors(skip=skip, limit=limit)
