from utils.database_nosql import get_db_nosql
from utils.database_sql import get_db_sql
from src.models.sql.student_model import Student
from src.models.sql.class_model import Class
from src.schemas.student_schema import *
from typing import Dict

def get_all_entities(entity_class):
    with next(get_db_sql()) as db_session:
        return db_session.query(entity_class).all()

def transform_student(student: Student) -> Dict:
    student_data = StudentSchema(
        student_id=student.id,
        last_name=student.last_name,
        first_name=student.first_name,
        date_of_birth=student.birth_date,
        address=student.address,
        gender=student.sex,
        student_class=transform_class(student.student_class) if student.student_class else None,
        grades=[transform_grade(grade) for grade in student.grades] if student.grades else []
    )
    return student_data.dict(by_alias=True)

def transform_class(cls: Class) -> Dict:
    class_data = ClassSchema(
        class_id=cls.id,
        name=cls.name,
        professor=transform_professor(cls.professor) if cls.professor else None
    )
    return class_data.dict(by_alias=True)

def transform_professor(professor) -> Dict:
    professor_data = ProfessorSchema(
        professor_id=professor.id,
        last_name=professor.last_name,
        first_name=professor.first_name,
        date_of_birth=professor.birth_date,
        address=professor.address,
        gender=professor.sex
    )
    return professor_data.dict(by_alias=True)

def transform_grade(grade) -> Dict:
    grade_data = GradeSchema(
        grade_id=grade.id,
        subject=transform_subject(grade.subject) if grade.subject else None,
        grade_value=grade.grade_value,
        date_entered=grade.entry_date,
        trimester=transform_trimester(grade.trimester) if grade.trimester else None,
        comment=grade.comment,
        progress=grade.progress
    )
    return grade_data.dict(by_alias=True)

def transform_subject(subject) -> Dict:
    subject_data = SubjectSchema(
        subject_id=subject.id,
        name=subject.name
    )
    return subject_data.dict(by_alias=True)

def transform_trimester(trimester) -> Dict:
    trimester_data = TrimesterSchema(
        trimester_id=trimester.id,
        name=trimester.name
    )
    return trimester_data.dict(by_alias=True)

# Function to migrate students from SQL to MongoDB
def migrate_students():
    # Get SQL data
    students = get_all_entities(Student)

    # Get MongoDB database instance
    mongodb = get_db_nosql()

    # Get or create the students collection
    students_collection = mongodb.get_collection("students")

    # Iterate over each student and migrate
    for student in students:
        transformed_data = transform_student(student)

        # Insert or update (upsert) the document in MongoDB
        try:
            students_collection.update_one(
                {"student_id": transformed_data["student_id"]},
                {"$set": transformed_data},
                upsert=True
            )
            print(f"Student {transformed_data['student_id']} migrated successfully.")
        except Exception as e:
            print(f"Error migrating student {transformed_data['student_id']}: {e}")

if __name__ == "__main__":
    # Call the migration function
    migrate_students()