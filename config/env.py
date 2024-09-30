"""
This script loads database configuration from a `.env` file using the `python-dotenv` library.

`load_dotenv()` makes these values accessible via `os.getenv()`.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Loads the environment from the file .env

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database_name = os.getenv("DB_NAME")

mongo_db = os.getenv("MONGO_URL")