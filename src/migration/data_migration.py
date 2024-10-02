from sqlalchemy.orm import Session
from pymongo import MongoClient
from utils.database_sql import get_db_sql
from utils.database_nosql import get_db_nosql
from src.models.student_model import Student
from src.migration.student_mapper import student_to_dict


def migrate_students():
    # Get the SQL and MongoDB connections
    sql_session: Session = next(get_db_sql())
    mongodb: MongoClient = get_db_nosql()

    # Specify the collection to insert data into
    students_collection = mongodb["students"]

    try:
        # Query all students from MariaDB
        students = sql_session.query(Student).all()

        for student in students:
            # Transform SQL data to the MongoDB schema format
            student_data = student_to_dict(student)

            # Insert transformed data into MongoDB
            try:
                students_collection.insert_one(student_data)
                print(f"Inserted student with ID: {student_data['student_id']}")
            except Exception as e:
                print(f"Failed to insert student with ID: {student_data['student_id']} - {e}")

    except Exception as e:
        print(f"Error during migration: {e}")

    finally:
        # Close the SQL session
        sql_session.close()


if __name__ == "__main__":
    migrate_students()
