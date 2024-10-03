# main.py

from fastapi import FastAPI

from src.routers.student_router import router as student_router
from src.routers.professor_router import router as professor_router

app = FastAPI()

# Register routers
app.include_router(professor_router)
app.include_router(student_router)

