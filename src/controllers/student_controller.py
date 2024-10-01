from typing import List
from src.schemas.grade_schema import GradeResponse, GradeSchema
from utils.database_nosql import get_db_nosql

def get_notes(last_name: str) -> List[GradeSchema]:

    # Connection to db
    db = get_db_nosql()

    # Connection to the collection
    students_coll = db['students']

    # Find the student by last name (case-insensitive search)
    searched_student = students_coll.find_one({'last_name': last_name.strip().title()})

    # If no student is found, return an empty list
    if not searched_student:
        return []

    # Retrieve the list of grades or return an empty list if "grades" key is not present
    grades_data = searched_student.get("grades", [])

    # Convert each grade dictionary to GradeResponse model
    return grades_data
