import unittest
from pymongo.errors import ConnectionFailure
from utils.database_nosql import get_db_nosql, get_db_nosql


class TestMongoDBConnection(unittest.TestCase):

    def test_mongo_connection_successful(self):
        """
        Test if the MongoDB connection is successful using the provided environment variables.
        """
        try:
            db = get_db_nosql()
            # Run a simple operation to test the connection
            db.command('ping')
            self.assertTrue(True)
        except ConnectionFailure:
            self.fail("MongoDB connection failed!")


if __name__ == '__main__':
    unittest.main()
