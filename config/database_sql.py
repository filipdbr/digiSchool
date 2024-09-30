"""
This module sets up the database connection and session for the application using SQLAlchemy.
It includes configuration for connecting to a MariaDB database and a function to manage database sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.env import username, password, host, port, database_name

# URL for the database connection
SQLALCHEMY_DATABASE_URL = f"mariadb+mariadbconnector://{username}:{password}@{host}:{port}/{database_name}"

# Create the engine that manages connections to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "SessionLocal" class
# Sessions created by this class will manage database transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db_sql():
    """
        Provides a database session for the duration of a request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()