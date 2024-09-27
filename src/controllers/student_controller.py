from sqlalchemy.orm import Session

from src.models.student import Student


def get_all_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()