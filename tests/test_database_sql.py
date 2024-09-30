import unittest

from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from utils.database_sql import get_db_sql

class TestSQLDatabaseConnection(unittest.TestCase):

    def test_sql_connection_successful(self):
        """
        Test if the SQL (MariaDB) connection is successful using the provided environment variables.
        """
        try:
            # Open a session with the database
            with next(get_db_sql()) as session:
                # Run a simple query to test the connection
                result = session.execute(text("SELECT 1")).scalar()
                self.assertEqual(result, 1)
        except OperationalError:
            self.fail("MariaDB connection failed!")

if __name__ == '__main__':
    unittest.main()
