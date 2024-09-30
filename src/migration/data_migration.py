from utils.database_nosql import get_db_nosql
from utils.database_sql import get_db_sql
from src.models.sql.student_model import Student

# Connect to both databases
maria_db = next(get_db_sql())
mongo_db = get_db_nosql()

students = maria_db.query(Student).all()
