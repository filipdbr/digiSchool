from fastapi import APIRouter, HTTPException, Query
from src.controllers.professor_controller import add_professor, find_professor_by_id, get_all_professors_controller, \
    update_professor_controller, patch_professor_controller, delete_professor_controller, \
    get_professors_with_students_and_grades_by_id
from src.schemas.professor_schema import ProfessorResponse, ProfessorAPI, ProfessorUpdateSchema
from typing import List, Dict

router = APIRouter(
    prefix="/professors",
    tags=["Professors"]
)

@router.post("/add")
def add_professor_to_classes(
    professor_data: ProfessorAPI,
    class_names: List[str] = Query(..., description="List of class names to assign the professor to")
):
    """
    Add a professor to specified classes.

    Put one or many classes names in the parameters.

    You can also add a new teacher to the class. Remember, there is only one teacher per class.
    """
    try:
        message = add_professor(professor_data, class_names)
        return {"message": message}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{id_prof}/info", response_model=ProfessorResponse)
def get_professor_by_id(id_prof: int):
    """
    Get info about a specific teacher. Find by ID.

    If in doubt of teacher's ID, use "View All Professors" function.
    """
    professor = find_professor_by_id(id_prof)
    return professor

@router.get("/get/all", response_model=List[ProfessorResponse])
def view_all_professors() -> list[ProfessorResponse]:
    """
    See all professors.
    """
    return get_all_professors_controller()

@router.get("/{professor_id}/students", response_model=Dict)
def get_students_with_grades_by_professor(professor_id: int):
    """
    TP: Récupérer les élèves et leur note selon un professeur

    Get the list of students with notes by professor ID.

    Comment: We provide user with partial inforation, which are interesting for the user. There is an option to add more data/info
    """

    try:
        data = get_professors_with_students_and_grades_by_id(professor_id)
        return data
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error in endpoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.patch("/update/details/{professor_id}")
def update_partially(professor_id: int, update_data: ProfessorUpdateSchema):
    """
    Update details of a professor.

    Please provide one or more fields to be updated.
    """
    try:
        updated_professor = patch_professor_controller(professor_id, update_data)
        return {
            "message": f"Professor ID: {professor_id} updated successfully.",
            "updated_professor": updated_professor
        }
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/update/{professor_id}")
def update_completely(professor_id: int, update_data: ProfessorUpdateSchema):
    """
    Update all thew details of a professor.

    The change of all details, you have to provide all fields
    """
    try:
        # Call the controller function to update the professor details
        result_message = update_professor_controller(professor_id, update_data)
        return {"message": result_message}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        # In case of unexpected error
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete/{professor_id}")
def delete_professor(professor_id: int):
    """
    Delete a professor by their ID.

    This action will remove the professor completely from the database.
    """
    try:
        delete_message = delete_professor_controller(professor_id)
        return {"message": delete_message}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))