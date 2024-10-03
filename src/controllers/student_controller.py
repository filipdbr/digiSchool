from src.schemas.grade_schema import GradeSchema
from typing import List, Optional
from src.schemas.student_schema import StudentSchema, StudentPatch, StudentResponse, StudentCreateSchema
from utils.database_nosql import get_db_nosql

# Database connection
db = get_db_nosql()
students_coll = db['students']


# create a student in the db
def create_student_controller(student: StudentCreateSchema) -> StudentResponse:
    # Convert the Pydantic model to a dict
    student_data = student.dict(exclude_unset=True)

    # Trim and format strings
    student_data['first_name'] = student_data['first_name'].strip().title()
    student_data['last_name'] = student_data['last_name'].strip().title()
    if 'address' in student_data and student_data['address']:
        student_data['address'] = student_data['address'].strip().title()
    student_data['gender'] = student_data['gender'].strip().upper()

    # Generate a new student_id
    max_student = students_coll.find_one(sort=[("student_id", -1)])
    new_student_id = (max_student["student_id"] if max_student else 0) + 1
    student_data["student_id"] = new_student_id

    # Initialize optional fields if needed
    student_data["grades"] = []  # Ensure 'grades' field exists
    # Do not include 'student_class' if it's None or not provided

    # Insert into the database
    result = students_coll.insert_one(student_data)

    # Return the created student data as StudentResponse
    return StudentResponse(**student_data)


# Read

# get all students
def get_all_students_controller():
    students = students_coll.find()
    return [StudentResponse(**student) for student in students]

# get by id
def get_student_by_id_controller(student_id: int) -> Optional[StudentResponse]:
    student_data = students_coll.find_one({"student_id": student_id})
    if student_data:
        return StudentResponse(**student_data)
    return f"Student with ID: {student_id} not found."


# find by last name
def find_student_by_last_name_controller(last_name: str) -> List[StudentResponse]:
    query = {"last_name": last_name.strip().title()}

    students_data = students_coll.find(query)

    return [StudentResponse(**student) for student in students_data] if students_data else []

# update student by ID
def update_student_controller(student_id: int, student: StudentCreateSchema) -> str:

    update_data = student.dict(exclude_unset=True)

    # Trim and format strings
    update_data['first_name'] = update_data['first_name'].strip().title()
    update_data['last_name'] = update_data['last_name'].strip().title()
    if 'address' in update_data and update_data['address']:
        update_data['address'] = update_data['address'].strip().title()
    update_data['gender'] = update_data['gender'].strip().upper()

    result = students_coll.update_one({"student_id": student_id}, {"$set": update_data})

    if result.modified_count > 0:
        return f"Student with ID: {student_id} updated successfully."

    return f"Student with ID: {student_id} not found or no changes made."


# Update certain details
def patch_student_controller(student_id: int, student_patch: StudentPatch) -> str:

    update_data = student_patch.dict(exclude_unset=True)

    # Trim and format strings
    update_data['first_name'] = update_data['first_name'].strip().title()
    update_data['last_name'] = update_data['last_name'].strip().title()
    if 'address' in update_data and update_data['address']:
        update_data['address'] = update_data['address'].strip().title()
    update_data['gender'] = update_data['gender'].strip().upper()

    result = students_coll.update_one({"student_id": student_id}, {"$set": update_data})
    if result.modified_count > 0:
        return f"Student with ID: {student_id} patched successfully."
    return f"Student with ID: {student_id} not found or no changes made."


# Delete student by ID
def delete_student_controller(student_id: int) -> str:
    result = students_coll.delete_one({"student_id": student_id})
    if result.deleted_count > 0:
        return f"Student with ID: {student_id} deleted successfully."
    return f"Student with ID: {student_id} not found."

# Get grades controller
def get_notes_controller(last_name: str) -> List[GradeSchema]:

    # Find the student by last name (case-insensitive search)
    searched_student = students_coll.find_one({'last_name': last_name.strip().title()})

    # If no student is found, return an empty list
    if not searched_student:
        return []

    # Retrieve the list of grades or return an empty list if "grades" key is not present
    grades_data = searched_student.get("grades", [])

    # Convert each grade dictionary to GradeResponse model
    return grades_data

# Get grades by id
def get_notes_by_id_controller(student_id: int) -> List[GradeSchema]:

    # Find the student by last name (case-insensitive search)
    searched_student = students_coll.find_one({'student_id': student_id})

    # If no student is found, return an empty list
    if not searched_student:
        return []

    # Retrieve the list of grades or return an empty list if "grades" key is not present
    grades_data = searched_student.get("grades", [])

    # Convert each grade dictionary to GradeResponse model
    return grades_data
