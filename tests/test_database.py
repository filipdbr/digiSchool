from sqlite3 import OperationalError
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from config.database import engine

import pytest


def test_db_connection():

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Connections successful")
    except OperationalError:
        pytest.fail("Database connection failed")