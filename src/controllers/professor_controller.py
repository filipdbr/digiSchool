"""
Retrieve the list of professors from student data using an aggregation pipeline.

This function connects to the MongoDB database, retrieves data from the 'students'
collection, and aggregates information about professors embedded within student records.
The output is a list of distinct professors.

Args:
    skip (int): The number of records to skip for pagination.
    limit (int): The maximum number of records to return for pagination.

Returns:
    List[dict]: A list of dictionaries containing professor information.
"""
from typing import List
from pymongo.collection import Collection
from utils.database_nosql import get_db_nosql
from src.schemas.professor_schema import ProfessorResponse

def get_all_professors(skip: int = 0, limit: int = 10) -> List[ProfessorResponse]:
    # Get MongoDB connection
    db = get_db_nosql()
    students_collection: Collection = db["students"]

    # Get all students with a professor
    students_cursor = students_collection.find({"student_class.professor": {"$exists": True}})

    # Use a set to store unique professors by their ID to avoid duplicates
    professors_set = {}

    # Iterate over students and collect unique professors
    for student in students_cursor:
        professor_data = student.get("student_class", {}).get("professor")
        if professor_data:
            professor_id = professor_data.get("teacher_id")
            if professor_id and professor_id not in professors_set:
                # Create a ProfessorResponse object without including the teacher_id
                professor = ProfessorResponse(
                    last_name=professor_data["last_name"],
                    first_name=professor_data["first_name"],
                    address=professor_data["address"],
                    gender=professor_data["gender"]
                )
                # Add professor to the set
                professors_set[professor_id] = professor

    # Convert to list for easy consumption and apply pagination
    professors_list = list(professors_set.values())

    # Apply pagination
    paginated_professors = professors_list[skip:skip + limit]

    return paginated_professors