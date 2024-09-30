from src.models.sql.student_model import Student
from src.schemas.class_schema import ClassSchema
from src.schemas.grade_schema import GradeSchema
from src.schemas.professor_schema import ProfessorSchema
from src.schemas.student_schema import StudentSchema
from src.schemas.subject_schema import SubjectSchema
from src.schemas.trimester_schema import TrimesterSchema


def student_to_dict(student: Student) -> dict:
    student_data = StudentSchema(
        student_id=student.student_id,
        last_name=student.last_name,
        first_name=student.first_name,
        birth_date=student.birth_date,
        address=student.address,
        gender=student.gender,
        student_class=ClassSchema(
            class_id=student.student_class.class_id,
            name=student.student_class.name,
            professor=ProfessorSchema(
                teacher_id=student.student_class.professor.teacher_id,
                last_name=student.student_class.professor.last_name,
                first_name=student.student_class.professor.first_name,
                date_of_birth=student.student_class.professor.birth_date,
                address=student.student_class.professor.address,
                gender=student.student_class.professor.gender
            ) if student.student_class.professor else None
        ) if student.student_class else None,
        grades=[
            GradeSchema(
                grade_id=grade.grade_id,
                subject=SubjectSchema(
                    subject_id=grade.subject.subject_id,
                    name=grade.subject.name
                ) if grade.subject else None,
                grade_value=grade.grade_value,
                date_entered=grade.date_entered,
                trimester=TrimesterSchema(
                    trimester_id=grade.trimester.trimester_id,
                    name=grade.trimester.name
                ) if grade.trimester else None,
                comment=grade.comment,
                progress=grade.progress
            )
            for grade in student.grades
        ] if student.grades else []
    )
    return student_data.model_dump()

