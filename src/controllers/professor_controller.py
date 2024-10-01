from typing import List

from fastapi import HTTPException
from pymongo.collection import Collection

from src.models import Professor
from utils.database_nosql import get_db_nosql
from src.schemas.professor_schema import ProfessorResponse, ProfessorSchema


# CRUD

# 1. Create methods

def add_professor(professor_data: ProfessorSchema, class_names: List[str]):

    # todo validation - there are duplicates

    # Connect to the database and collections
    db = get_db_nosql()
    students_coll = db['students']

    # Create the new professor object
    new_professor = professor_data.dict(exclude_unset=True)

    total_updated = 0
    for class_name in class_names:
        # Update all students in the specified class to assign them the new professor
        update_result = students_coll.update_many(
            {"student_class.name": class_name.upper()},  # Find students who are in the specified class
            {"$set": {"student_class.professor": new_professor}}  # Set the professor details for the specified class
        )

        total_updated += update_result.modified_count

        # Check if the update was successful for each class
        if update_result.modified_count > 0:
            print(f"Assigned new professor to {update_result.modified_count} students in class '{class_name}'.")
        else:
            print(f"No students found in class '{class_name}'. Professor not added to this class.")

    if total_updated == 0:
        raise ValueError(f"No students found in any of the specified classes. Professor not added.")

    return f"Assigned new professor to a total of {total_updated} students in classes {', '.join(class_names).upper()}."

# 2. Read methods

def find_professor_by_id(id_prof: int) -> ProfessorResponse:
    """
    Find professor by ID.
    """
    # Connect to DB
    db = get_db_nosql()
    students_coll = db['students']

    # Search professor by teacher_id
    professor_data = students_coll.find_one({"student_class.professor.teacher_id": id_prof})

    # Raise error if not found
    if professor_data is None:
        raise HTTPException(status_code=404, detail=f"No professor with id {id_prof} found.")

    # Get professor info
    professor_info = professor_data.get("student_class", {}).get("professor", {})

    # Create response object
    professor = ProfessorResponse(**professor_info)

    return professor


def get_all_professors_controller() -> List[ProfessorResponse]:
    """
    Retrieve all professors.
    """
    # Connect to DB
    db = get_db_nosql()
    students_coll = db['students']

    # Retrieve all students
    students = students_coll.find()

    # Track existing professors using a set of unique IDs
    existing_professors = set()
    professors_list = []

    # Iterate through all students to collect unique professors
    for student in students:
        professor = student.get("student_class", {}).get("professor", {})

        # Ensure professor data is present
        if professor and professor.get("teacher_id"):
            prof_id = professor["teacher_id"]

            # Add to set if not already added
            if prof_id not in existing_professors:
                existing_professors.add(prof_id)

                # Create a ProfessorResponse object
                professor_obj = ProfessorResponse(**professor)
                professors_list.append(professor_obj)

    return professors_list


