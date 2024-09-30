import pytest
from datetime import datetime
from src.schemas.class_schema import ClassSchema
from src.schemas.grade_schema import GradeSchema
from src.schemas.professor_schema import ProfessorSchema
from src.schemas.subject_schema import SubjectSchema
from src.schemas.trimester_schema import TrimesterSchema
from src.migration.data_migration import student_to_dict
from src.models.sql.student_model import Student
from src.models.sql.class_model import Class
from src.models.sql.professor_model import Professor
from src.models.sql.grade_model import Grade
from src.models.sql.subject_model import Subject
from src.models.sql.trimester_model import Trimester



# Mock data setup
def create_mock_student():
    return Student(
        student_id=1,
        last_name='Doe',
        first_name='John',
        birth_date=datetime(2000, 1, 1),
        address='123 Main St',
        gender='HOMME',
        student_class=Class(
            class_id=101,
            name='Mathematics',
            professor=Professor(
                teacher_id=201,
                last_name='Smith',
                first_name='Jane',
                birth_date=datetime(1980, 5, 15),
                address='456 Secondary St',
                gender='FEMME'
            )
        ),
        grades=[
            Grade(
                grade_id=301,
                subject=Subject(
                    subject_id=401,
                    name='Algebra'
                ),
                grade_value=90.0,
                date_entered=datetime.now(),
                trimester=Trimester(
                    trimester_id=501,
                    name='First Trimester'
                ),
                comment='Great job!',
                progress=0.85
            )
        ]
    )

def test_student_to_dict():
    student = create_mock_student()
    student_dict = student_to_dict(student)

    assert student_dict['student_id'] == 1
    assert student_dict['last_name'] == 'Doe'
    assert student_dict['first_name'] == 'John'
    assert student_dict['student_class']['name'] == 'Mathematics'
    assert student_dict['student_class']['professor']['last_name'] == 'Smith'
    assert student_dict['grades'][0]['grade_value'] == 90
    assert student_dict['grades'][0]['subject']['name'] == 'Algebra'

    print(student_dict)
