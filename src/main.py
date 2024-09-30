from fastapi import FastAPI
from src.models.sql.base_model import Base
from utils.database_sql import engine
from src.routers import student_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(student_router.router)

@app.get("/")
def home():
    return {"Hello": "World"}