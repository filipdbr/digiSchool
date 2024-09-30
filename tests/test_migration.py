# test_migration.py
import pytest
from utils.database_sql import get_db_sql
from utils.database_nosql import get_db_nosql
from src.models.sql.student_model import Student
from src.migration.data_migration import transform_student
from pymongo.errors import DuplicateKeyError

# SQL and NoSQL Database Connections
@pytest.fixture
def sql_session():
    """
    Fixture to provide an SQLAlchemy session.
    """
    session = next(get_db_sql())
    yield session
    session.close()

@pytest.fixture
def mongo_db():
    """
    Fixture to provide a MongoDB client.
    """
    return get_db_nosql()

def test_migration(sql_session, mongo_db):
    """
    Test function to migrate a sample of student data from SQL to MongoDB.
    """
    # Fetch a sample of data from SQL
    try:
        students = sql_session.query(Student).limit(5).all()  # Limit to 5 students for testing
        for student in students:
            # Transform SQL data to MongoDB schema format
            student_data = transform_student(student)

            # Insert into MongoDB (avoid duplicate insertions)
            try:
                mongo_db["students"].insert_one(student_data)
                print(f"Inserted student with ID: {student_data['student_id']}")
            except DuplicateKeyError:
                print(f"Student with ID: {student_data['student_id']} already exists in MongoDB.")

    except Exception as e:
        pytest.fail(f"Error during migration: {e}")
