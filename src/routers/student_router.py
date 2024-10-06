from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Union, Dict

from src.controllers.student_controller import get_all_students_controller, get_notes_by_id_controller, \
    get_all_students_with_grades_controller
from src.schemas.student_schema import StudentSchema, StudentPatch, StudentResponse, StudentCreateSchema
from src.schemas.grade_schema import GradeSchema
from src.controllers import create_student_controller, get_student_by_id_controller, \
    find_student_by_last_name_controller, update_student_controller, patch_student_controller, \
    delete_student_controller, get_notes_controller

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/create", response_model=StudentResponse)
def add_student(student: StudentCreateSchema):
    return create_student_controller(student)

@router.get("/get/all", response_model=List[StudentResponse])
def see_all_students():
    """
    View all students
    """
    return get_all_students_controller()

@router.get("/get/all/grades", response_model=Dict)
def see_all_students_with_grades():
    """
    Showing basic info of the student + info of the grades
    """
    students = get_all_students_with_grades_controller()
    if not students:
        raise HTTPException(status_code=404, detail="Didin't find any students")
    return students

@router.get("/get/id/{student_id}", response_model=Union[StudentResponse, str])
def find_student_by_id(student_id: int):
    """
    Find a student by ID.
    """
    student = get_student_by_id_controller(student_id)
    if isinstance(student, str):
        raise HTTPException(status_code=404, detail=student)
    return student


@router.get("/get/by/name/{last_name}", response_model=List[StudentResponse])
def find_student_by_last_name(last_name: str):
    """
    Find a student by last name. Optionally you can add first name (put it in the parameter).
    """
    last_name = last_name.strip().title()

    students = find_student_by_last_name_controller(last_name)

    if not students:
        raise HTTPException(status_code=404, detail="No students found with the provided name.")
    return students


# GET NOTES by Last Name
@router.get("/grades/by/name/{last_name}", response_model=List[GradeSchema])
def get_grades_by_last_name(last_name: str):
    """
    TP: Récupérer les notes d 'un élève (ici par le nom d 'un élève)

    Get student grades by last name.
    """
    grades = get_notes_controller(last_name)
    if not grades:
        raise HTTPException(status_code=404, detail="Student with the given last name not found or no grades available.")
    return grades

# GET NOTES by ID
@router.get("/grades/by/id/{student_id}", response_model=List[GradeSchema])
def get_grades_by_id(student_id: int):
    """
    TP: Récupérer les notes d 'un élève (ici par ID)

    Get student grades by ID
    """
    grades = get_notes_by_id_controller(student_id)
    if not grades:
        raise HTTPException(status_code=404, detail="Student with the given ID not found or no grades available.")
    return grades

@router.put("/student/{student_id}", response_model=str)
def update_student_details(student_id: int, student: StudentCreateSchema):
    """
    Update student data. Provide all mandatory data.

    Put student ID as a parameter.
    """
    result = update_student_controller(student_id, student)
    if "not found" in result:
        raise HTTPException(status_code=404, detail=result)
    return result

# PATCH
@router.patch("/student/{student_id}", response_model=str)
def update_student_details(student_id: int, student_patch: StudentPatch):
    """
    You can update only part of student data here. All data is optional
    """
    result = patch_student_controller(student_id, student_patch)
    if "not found" in result:
        raise HTTPException(status_code=404, detail=result)
    return result

@router.delete("/student/{student_id}", response_model=str)
def delete_student(student_id: int):
    """
    Delete student by ID.
    """
    result = delete_student_controller(student_id)
    if "not found" in result:
        raise HTTPException(status_code=404, detail=result)
    return result
