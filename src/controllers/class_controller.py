from typing import Dict, List
from fastapi import HTTPException
from utils.database_nosql import get_db_nosql


def get_all_classes_with_students() -> List[Dict]:
    # Connect to DB
    db = get_db_nosql()
    students_coll = db['students']
    try:
        pipeline = [
            {
                "$match": {  # Filter students with valid class_id and class_name
                    "student_class.class_id": {"$exists": True, "$ne": None},
                    "student_class.name": {"$exists": True, "$ne": ""}
                }
            },
            {
                "$group": {  # Group students by class_id and class_name
                    "_id": {
                        "class_id": "$student_class.class_id",
                        "class_name": "$student_class.name"
                    },
                    "students": {  # Collect students' basic info
                        "$push": {
                            "student_id": "$student_id",
                            "last_name": "$last_name",
                            "first_name": "$first_name"
                        }
                    }
                }
            },
            {
                "$project": {  # Format the output structure
                    "_id": 0,
                    "class_id": "$_id.class_id",
                    "class_name": "$_id.class_name",
                    "students": 1
                }
            },
            {
                "$sort": {  # Sort classes by class_id in ascending order
                    "class_id": 1
                }
            }
        ]
        classes = list(students_coll.aggregate(pipeline))  # Execute aggregation
        if not classes:
            raise HTTPException(status_code=404, detail="No classes found.")
        return classes
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error fetching classes with students: {e}")  # Log error message
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Note: The following definition of get_all_classes_with_students is duplicated.
# Ensure to remove one of them to avoid conflicts.

def get_all_classes_with_students() -> List[Dict]:
    db = get_db_nosql()
    students_coll = db['students']
    try:
        pipeline = [
            {
                "$match": {  # Filter students with valid class_id and class_name
                    "student_class.class_id": {"$exists": True, "$ne": None},
                    "student_class.name": {"$exists": True, "$ne": ""}
                }
            },
            {
                "$group": {  # Group students by class_id and class_name
                    "_id": {
                        "class_id": "$student_class.class_id",
                        "class_name": "$student_class.name"
                    },
                    "students": {  # Collect students' basic info
                        "$push": {
                            "student_id": "$student_id",
                            "last_name": "$last_name",
                            "first_name": "$first_name"
                        }
                    }
                }
            },
            {
                "$project": {  # Format the output structure
                    "_id": 0,
                    "class_id": "$_id.class_id",
                    "class_name": "$_id.class_name",
                    "students": 1
                }
            },
            {
                "$sort": {  # Sort classes by class_id in ascending order
                    "class_id": 1
                }
            }
        ]
        classes = list(students_coll.aggregate(pipeline))  # Execute aggregation
        if not classes:
            raise HTTPException(status_code=404, detail="No classes found.")
        return classes
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error fetching classes with students: {e}")  # Log error message
        raise HTTPException(status_code=500, detail="Internal Server Error")


def get_students_by_class_id(class_id: int) -> Dict:
    db = get_db_nosql()
    students_coll = db['students']
    try:
        query = {"student_class.class_id": class_id}  # Filter by class_id

        students = list(students_coll.find(query))  # Retrieve matching students

        if not students:
            raise HTTPException(status_code=404, detail=f"No class found with ID '{class_id}' or no students.")

        first_student = students[0]
        student_class = first_student.get('student_class', {})

        class_data = {
            "class_id": student_class.get("class_id"),
            "class_name": student_class.get("name"),
            "students": []
        }

        unique_students = {}
        for student in students:
            student_id = student.get("student_id")
            if student_id not in unique_students:
                student_data = {
                    "student_id": student_id,
                    "last_name": student.get("last_name"),
                    "first_name": student.get("first_name")
                }
                unique_students[student_id] = student_data

        class_data["students"] = list(unique_students.values())  # Assign unique students
        return class_data
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error fetching students by class_id: {e}")  # Log error message
        raise HTTPException(status_code=500, detail="Internal Server Error")


def get_students_by_class_name(class_name: str) -> Dict:
    db = get_db_nosql()
    students_coll = db['students']
    try:
        query = {"student_class.name": class_name.strip().upper()}  # Filter by class_name

        students = list(students_coll.find(query))  # Retrieve matching students

        if not students:
            raise HTTPException(status_code=404, detail=f"No class found with name '{class_name}' or no students.")

        first_student = students[0]
        student_class = first_student.get('student_class', {})

        class_data = {
            "class_id": student_class.get("class_id"),
            "class_name": student_class.get("name"),
            "students": []
        }

        unique_students = {}
        for student in students:
            student_id = student.get("student_id")
            if student_id not in unique_students:
                student_data = {
                    "student_id": student_id,
                    "last_name": student.get("last_name"),
                    "first_name": student.get("first_name")
                }
                unique_students[student_id] = student_data

        class_data["students"] = list(unique_students.values())  # Assign unique students
        return class_data
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error fetching students by class_name: {e}")  # Log error message
        raise HTTPException(status_code=500, detail="Internal Server Error")
