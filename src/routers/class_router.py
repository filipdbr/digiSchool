# src/routes/class_router.py

from fastapi import APIRouter, HTTPException
from typing import Dict, List
from src.controllers.class_controller import (
    get_all_classes_with_students,
    get_students_by_class_id,
    get_students_by_class_name
)

router = APIRouter(
    prefix="/classes",
    tags=["Classes"]
)

@router.get("/students", response_model=List[Dict])
def get_students():
    """
    TP: Récupérer la liste des élèves par classe

    See all classes and list of students per class
    """
    try:
        classes = get_all_classes_with_students()
        return classes
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error in endpoint retrieve_all_classes: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/id/{class_id}/students", response_model=Dict)
def get_students_by_class_id(class_id: int):
    """
    TP: Récupérer la liste des élèves selon le choix d’une classe

    Get all students per class by class ID.
    """
    try:
        data = get_students_by_class_id(class_id)
        return data
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error in endpoint retrieve_students_by_class_id: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/name/{class_name}/students", response_model=Dict)
def retrieve_students_by_class_name(class_name: str):
    """
    TP: Récupérer la liste des élèves selon le choix d’une classe

    Get all students per class by class name.
    """
    try:
        data = get_students_by_class_name(class_name)
        return data
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error in endpoint retrieve_students_by_class_name: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
