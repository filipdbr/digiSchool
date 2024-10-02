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
    try:
        for student in existing_students:
            student_class = student.get("student_class", {})
            class_name = student_class.get("name")
            if class_name:
                existing_class_names.add(class_name.upper())

        # Convert set to list for further operations
        existing_class_names_list = list(existing_class_names)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while collecting class information: {str(e)}")

    # Validate professor existence by name and surname
    existing_professor = students_coll.find_one({
        "student_class.professor.last_name": professor_data.last_name.strip().title(),
        "student_class.professor.first_name": professor_data.first_name.strip().title()
    })

    if existing_professor:
        existing_professor_id = existing_professor["student_class"]["professor"]["professor_id"]
        raise HTTPException(
            status_code=400,
            detail=f"The professor '{professor_data.last_name}', '{professor_data.first_name}' already exists in the database. "
                   f"Professor's ID is '{existing_professor_id}'. In order to attribute teacher to classes, modify the existing teacher instead of creating a new one."
        )

    # Validate that all provided classes exist
    for class_name in class_names:
        if class_name.upper() not in existing_class_names_list:
            raise HTTPException(
                status_code=404,
                detail=f"Class '{class_name.upper()}' doesn't exist."
            )
