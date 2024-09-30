"""
This module sets up the MongoDB connection for the application using PyMongo.
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the mongo from environment variables
mongo_url = os.getenv('MONGO_URL')

# create MongoDB client
client = MongoClient(mongo_url)

# Get the database
mongodb = client.get_database()

# Function to get the connection
def get_mongo_db():
    """
    Provides a MongoDB connection
    """
    return mongodb