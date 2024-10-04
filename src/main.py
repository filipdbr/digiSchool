from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.routers.student_router import router as student_router
from src.routers.professor_router import router as professor_router
from src.routers.class_router import router as class_router

app = FastAPI()

# main page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to DigiSchool</title>
    </head>
    <body>
        <h1>Welcome to DigiSchool FastAPI App</h1>
        <p>To explore and test the API endpoints, visit <a href="/docs">/docs</a>.</p>
    </body>
    </html>
    """

# routers
app.include_router(student_router)
app.include_router(professor_router)
app.include_router(class_router)
