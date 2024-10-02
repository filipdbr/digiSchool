from typing import List

from fastapi import HTTPException
from pymongo.collection import Collection

from src.models import Professor
from src.services.professor_service import validate_professor
from utils.database_nosql import get_db_nosql
from src.schemas.professor_schema import ProfessorResponse, ProfessorSchema


# CRUD

# 1. Create methods

def add_professor(professor_data: ProfessorSchema, class_names: List[str]):

    # Professor validation
    validate_professor(professor_data, class_names)

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

    return f"Assigned new professor to a total of {total_updated} students in class(es) {', '.join(class_names).upper()}."

# 2. Read methods

def find_professor_by_id(id_prof: int) -> ProfessorResponse:
    """
    Find professor by ID along with their assigned classes.
    """
    # Connect to DB
    db = get_db_nosql()
    students_coll = db['students']

    # Retrieve all students where the professor has the given teacher_id
    students_with_professor = students_coll.find({"student_class.professor.teacher_id": id_prof})

    # Initialize variables to store professor data and their assigned classes
    professor_info = None
    classes = []

    # Iterate over all students with the given professor ID to collect data and classes
    for student in students_with_professor:
        student_class = student.get("student_class", {})
        professor = student_class.get("professor", {})

        # Set professor_info from the first occurrence
        if not professor_info:
            professor_info = professor

        # Collect class names for the professor
        class_name = student_class.get("name")
        if class_name and class_name not in classes:
            classes.append(class_name)

    # Raise error if no professor data found
    if professor_info is None:
        raise HTTPException(status_code=404, detail=f"No professor with id {id_prof} found.")

    # Create response object with professor information and assigned classes
    professor = ProfessorResponse(
        **professor_info,
        classes=classes
    )

    return professor


def get_all_professors_controller() -> List[ProfessorResponse]:
    """
    Retrieve all professors along with their assigned classes.
    """
    # Connect to DB
    db = get_db_nosql()
    students_coll = db['students']

    # Retrieve all students
    students = students_coll.find()

    # Track existing professors using a dictionary to collect their classes
    existing_professors = {}

    # Iterate through all students to collect unique professors and their classes
    for student in students:
        student_class = student.get("student_class", {})
        professor = student_class.get("professor", {})

        # Ensure professor data is present
        if professor and professor.get("teacher_id"):
            prof_id = professor["teacher_id"]
            class_name = student_class.get("name")

            # If professor is already tracked, add the class to their list of classes
            if prof_id in existing_professors:
                if class_name and class_name not in existing_professors[prof_id]["classes"]:
                    existing_professors[prof_id]["classes"].append(class_name)
            else:
                # Track new professor and initialize their classes list
                existing_professors[prof_id] = {
                    "professor_data": professor,
                    "classes": [class_name] if class_name else []
                }

    # Create a list of ProfessorResponse objects
    professors_list = []
    for prof_id, prof_info in existing_professors.items():
        professor_data = prof_info["professor_data"]
        classes = prof_info["classes"]

        # Create a ProfessorResponse object and add classes
        professor_obj = ProfessorResponse(
            **professor_data,
            classes=classes
        )
        professors_list.append(professor_obj)

    return professors_list



