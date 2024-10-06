from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.migration.data_migration import migrate_students
from src.routers.student_router import router as student_router
from src.routers.professor_router import router as professor_router
from src.routers.class_router import router as class_router
from utils.setup_mongodb import setup_mongodb

app = FastAPI()

# Initialize the database setup and migration
def initialize_app():
    try:
        # Step 1: Setup MongoDB - create collections with validation
        setup_mongodb()
        print("MongoDB setup completed.")

        # Step 2: Migrate data from SQL to MongoDB
        migrate_students()
        print("Data migration completed.")

    except Exception as e:
        print(f"Initialization error: {e}")

# Call the initialization function at startup
initialize_app()

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
        <h1>Welcome to DigiSchool FastAPI App by Filip et Marwa</h1>
        <p>To explore and test the API endpoints, visit <a href="/docs">/docs</a>.</p>
    </body>
    </html>
    """

# routers
app.include_router(student_router)
app.include_router(professor_router)
app.include_router(class_router)
