# main.py

from fastapi import FastAPI
from src.routers.professor_router import router as professor_router

app = FastAPI()

# Register routers
app.include_router(professor_router)

