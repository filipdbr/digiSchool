from fastapi import APIRouter, HTTPException, Query
from src.controllers.professor_controller import add_professor, find_professor_by_id, get_all_professors_controller
from src.schemas.professor_schema import ProfessorSchema, ProfessorResponse
from typing import List

router = APIRouter(
    prefix="/professors",
    tags=["professors"]
)

@router.post("/add")
def add_professor_to_classes(
    professor_data: ProfessorSchema,
    class_names: List[str] = Query(..., description="List of class names to assign the professor to")
):
    """
    Add a professor to specified classes and assign them to all students in those classes.

    Put class or classes names in the parameters.
    """
    try:
        message = add_professor(professor_data, class_names)
        return {"message": message}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{id_prof}/info", response_model=ProfessorResponse)
def get_professor_by_id(id_prof: int):
    """
    Endpoint to retrieve a professor by their ID.
    """
    professor = find_professor_by_id(id_prof)
    return professor

@router.get("/all", response_model=List[ProfessorResponse])
def get_all_professors() -> list[ProfessorResponse]:
    """
    Endpoint to retrieve all professors.
    """
    return get_all_professors_controller()
