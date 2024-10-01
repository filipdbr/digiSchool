from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.schemas.grade_schema import GradeResponse
from src.controllers.student_controller import get_notes

router = APIRouter()

@router.get("/student/grades", response_model=List[GradeResponse])
def get_student_grades(last_name: str = Query(...)):
    grades = get_notes(last_name=last_name)

    if not grades:
        raise HTTPException(status_code=404, detail="Student with the given last name not found")

    return grades
