from config.database_sql import get_db
from src.models.sql.student_model import Student

class TestStudent:
    """
    A simple test class to check if the Student model maps correctly to the database.
    """

    def setup_method(self):
        # Initialize the session using get_db()
        self.db = next(get_db())

    def teardown_method(self):
        # Close the database session after each test
        self.db.close()

    def test_get_student_by_nom(self):
        """
        Fetch a student by the 'nom' attribute and check if it exists.
        """
        student = self.db.query(Student).filter(Student.nom == "Eto").first()
        assert student is not None, f"No student found with the name 'Eto'"
        assert student.prenom is not None
        print(f"Student found: {student.prenom} {student.nom}")


# Usage example
if __name__ == "__main__":
    # Create an instance of the test class
    student_test = TestStudent()

    # Test the get_student_by_nom function
    student_test.get_student_by_nom()
