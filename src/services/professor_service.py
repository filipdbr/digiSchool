from fastapi import HTTPException
from utils.database_nosql import get_db_nosql
from src.schemas.professor_schema import ProfessorSchema
from typing import List


def validate_professor(professor_data: ProfessorSchema, class_names: List[str]):
    """
    Validates if a professor with the given name and surname already exists
    and if the class names are valid. Prints the list of all existing classes at the end.
    """
    # Connect to the MongoDB collection
    db = get_db_nosql()
    students_coll = db['students']

    # Retrieve all existing classes from student documents
    existing_students = students_coll.find()
    existing_class_names = set()

    # Collect unique class names
    for student in existing_students:
        student_class = student.get("student_class", {})
        class_name = student_class.get("name")
        if class_name:
            existing_class_names.add(class_name.upper())

    # Convert set to list for further operations
    existing_class_names_list = list(existing_class_names)

    # Validate professor existence by name and surname
    existing_professors = students_coll.find({
        "student_class.professor.last_name": professor_data.last_name.strip().upper(),
        "student_class.professor.first_name": professor_data.first_name.strip().capitalize()
    })

    # Create a set to collect unique IDs of existing professors
    existing_professor_ids = {
        student["student_class"]["professor"]["teacher_id"]
        for student in existing_professors
        if "student_class" in student and "professor" in student["student_class"] and "teacher_id" in
           student["student_class"]["professor"]
    }

    # If professor with the same name and surname exists but has a different ID
    if existing_professor_ids:
        # Check if the current professor ID matches any existing ID
        if professor_data.teacher_id not in existing_professor_ids:
            existing_professor_ids_str = ', '.join(map(str, existing_professor_ids))
            raise HTTPException(
                status_code=400,
                detail=f"The professor '{professor_data.last_name}', '{professor_data.first_name}' already exists in the database with a different ID. "
                       f"Existing professor's ID: {existing_professor_ids_str}. Please use the existing professor ID to update the class or modify the existing professor to change id."
            )

    # Validate that all provided classes exist
    for class_name in class_names:
        if class_name.upper() not in existing_class_names_list:
            raise HTTPException(
                status_code=404,
                detail=f"Class '{class_name}' doesn't exist. Existing classes: {', '.join(existing_class_names_list)}."
            )

def validate_professor_duplicates(professor_data: ProfessorSchema):
    """
    Validates if a professor with the given name and surname already exists in the database.
    """
    # Connect to the MongoDB collection
    db = get_db_nosql()
    students_coll = db['students']

    # Check if a professor with the same first name and last name already exists
    existing_professor = students_coll.find_one({
        "student_class.professor.last_name": professor_data.last_name.strip().upper(),
        "student_class.professor.first_name": professor_data.first_name.strip().capitalize()
    })

    # Raise an exception if a professor with the same first name and last name already exists
    if existing_professor:
        raise HTTPException(
            status_code=400,
            detail=f"A professor with the name '{professor_data.first_name} {professor_data.last_name}' already exists in the database."
        )