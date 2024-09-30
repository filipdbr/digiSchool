from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.controllers import student_controller

from config.database import get_db
from src.schemas.student_schema import StudentSchema, StudentResponseSchema, StudentResponseSchema

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=list[StudentResponseSchema])
def get_all_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return student_controller.get_all_students(skip=skip, limit=limit, db=db)