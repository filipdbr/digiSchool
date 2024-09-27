from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.env import username, password, host, port, database_name

# URL of a database connection
SQLALCHEMY_DATABASE_URL = f"mariadb+pymariadb://{username}:{password}@{host}:{port}/{database_name}"

# Permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db # couplé avec Depends de fastapi
    finally:
        db.close()