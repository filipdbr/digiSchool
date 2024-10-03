from typing import List
from fastapi import HTTPException
from src.services.professor_service import validate_professor, validate_professor_duplicates
from utils.database_nosql import get_db_nosql
from src.schemas.professor_schema import ProfessorResponse, ProfessorSchema, ProfessorUpdateSchema


# CRUD

# 1. Create methods

def add_professor(professor_data: ProfessorSchema, class_names: List[str]):
    """
    Add professor the class or classes. Will be used for PUT endpoint.

    Which is important, is that in the app cannot exist a teacher without a class. Hence if we want to create a new teacher,
    we need to either replace a current teacher which teaching a class (in the school), or create a new students class.
    One of the assumptions is that there is no teacher without a students' class attached.
    """

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
    Find professor by ID along with their assigned classes. Will be used for GET endpoint.
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

# 3. Update method

def patch_professor_controller(professor_id: int, update_data: ProfessorUpdateSchema) -> dict:
    """
    Updates professor details (excluding 'teacher_id' and 'classes') in all student records.
    Returns the updated professor details.
    """
    # Connect to the database
    db = get_db_nosql()
    students_coll = db['students']

    # Duplicates validation
    validate_professor_duplicates(professor_data=update_data)

    # Find the professor in student records and update the details
    prof = {"student_class.professor.teacher_id": professor_id}

    # Create update values dynamically based on non-null values in update_data
    update_values = {}

    if update_data.last_name is not None:
        update_values["student_class.professor.last_name"] = update_data.last_name.strip().title()

    if update_data.first_name is not None:
        update_values["student_class.professor.first_name"] = update_data.first_name.strip().title()

    if update_data.date_of_birth is not None:
        update_values["student_class.professor.date_of_birth"] = update_data.date_of_birth

    if update_data.address is not None:
        update_values["student_class.professor.address"] = update_data.address.capitalize()

    if update_data.gender is not None:
        update_values["student_class.professor.gender"] = update_data.gender.upper()

    # Perform the update only if there are fields to update
    if update_values:
        students_coll.update_many(prof, {"$set": update_values})

    # Find and return the updated professor details
    updated_prof = students_coll.find_one(prof, {"_id": 0, "student_class.professor": 1})

    if updated_prof and "student_class" in updated_prof and "professor" in updated_prof["student_class"]:
        return updated_prof["student_class"]["professor"]
    else:
        raise ValueError(f"Professor with ID {professor_id} not found.")

def update_professor_controller(professor_id: int, update_data: ProfessorUpdateSchema) -> str:
    """
    Updates professor details (excluding 'teacher_id' and 'classes') in all student records.
    """
    # Duplicates validation
    validate_professor_duplicates(professor_data=update_data)

    # Connect to the database
    db = get_db_nosql()
    students_coll = db['students']

    # Find the professor in student records and update the details
    prof_filter = {"student_class.professor.teacher_id": professor_id}

    # Create update values with all provided data
    update_values = {
        "student_class.professor.last_name": update_data.last_name.strip().title() if update_data.last_name else None,
        "student_class.professor.first_name": update_data.first_name.strip().title() if update_data.first_name else None,
        "student_class.professor.date_of_birth": update_data.date_of_birth,
        "student_class.professor.address": update_data.address.strip().capitalize() if update_data.address else None,
        "student_class.professor.gender": update_data.gender.strip().upper() if update_data.gender else None,
    }

    # Remove fields that are None to avoid overwriting existing data with null values
    update_values = {key: value for key, value in update_values.items() if value is not None}

    # Perform the update
    if update_values:
        result = students_coll.update_many(prof_filter, {"$set": update_values})

        # Check if any document was modified
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail=f"No professor found with ID {professor_id} to update.")

    return f"Professor ID {professor_id} updated successfully."


def delete_professor_controller(professor_id: int) -> str:
    """
    Delete a professor by their ID.

    Removes professor details from all students' records where they are assigned.
    """
    # Connect to the database
    db = get_db_nosql()
    students_coll = db['students']

    # Find the professor in student records
    prof_filter = {"student_class.professor.teacher_id": professor_id}

    # Perform the update to remove the professor details
    update_result = students_coll.update_many(
        prof_filter,
        {"$unset": {"student_class.professor": ""}}
    )

    # Check if any document was modified
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail=f"No professor found with ID {professor_id} to delete.")

    # Check for classes without a professor assigned
    classes_without_professor = students_coll.distinct("student_class.name",
                                                       {"student_class.professor": {"$exists": False}})

    # Create the return message
    message = f"Professor ID {professor_id} deleted successfully from {update_result.modified_count} student records."

    if classes_without_professor:
        classes_list = ', '.join(classes_without_professor)
        message += f" Note: The following classes do not have a professor assigned: {classes_list}."

    return message






