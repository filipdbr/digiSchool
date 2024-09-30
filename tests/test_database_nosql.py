import unittest
from pymongo.errors import ConnectionFailure
from config.database_nosql import get_mongo_db


class TestMongoDBConnection(unittest.TestCase):

    def test_mongo_connection_successful(self):
        """
        Test if the MongoDB connection is successful using the provided environment variables.
        """
        try:
            db = get_mongo_db()
            # Run a simple operation to test the connection
            db.command('ping')
            self.assertTrue(True)
        except ConnectionFailure:
            self.fail("MongoDB connection failed!")


if __name__ == '__main__':
    unittest.main()
