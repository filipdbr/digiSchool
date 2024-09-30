## *This is a draft*

## How to set up the project? 

#### 1. Clone the repository
```bash
1. git clone <repository-url>
cd <repository-directory>
```

#### 2. Set Up the virtual environment and dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set up environment variables

Copy the `.env.template` file and rename it to `.env`  
Fill in the values as per the instructions provided in the `.env.template`
#### 5. Run the app

```bash
python run.py
```

## Project structure

Find the structure of the project below:

```bash
my_app/
│
├── main.py                        # Main entry point for the application
├── config/
│   ├── database.py                # Database configuration (SQL and NoSQL)
│   ├── env.py                     # Environment variables management
│   └── settings.py                # Global application settings
│
├── src/
│   ├── controllers/               # Business logic (CRUD operations and migration)
│   │   ├── student_controller.py  # CRUD operations for student data
│   │   ├── notes_controller.py    # CRUD operations for notes
│   │   └── migration_controller.py# Migration from SQL to MongoDB
│   │
│   ├── models/                    # Data models
│   │   ├── sql/                   # SQLAlchemy ORM models (for migration)
│   │   │   ├── base_model.py      # Base class for SQLAlchemy models
│   │   │   ├── student.py         # SQL model for students
│   │   │   ├── classe.py          # SQL model for classes
│   │   │   ├── professor.py       # SQL model for professors
│   │   │   └── notes.py           # SQL model for notes
│   │   │
│   │   └── nosql/                 # Data models for MongoDB (optional)
│   │       ├── student.py         # Model representing student document structure
│   │
│   ├── schemas/                   # Pydantic schemas (input/output data validation)
│   │   ├── student.py             # Schemas for student operations
│   │   └── migration.py           # Schemas for migration (optional)
│   │
│   ├── routers/                   # API endpoints (user access)
│   │   ├── student_router.py      # CRUD endpoints for students
│   │   └── migration_router.py    # Endpoints for data migration
│   │
│   ├── services/                  # Intermediate logic for interacting with NoSQL database (optional)
│   │   ├── student_service.py     # Service for student operations (MongoDB)
│   │
│   └── utils/                     # Utility tools
│       └── db_utils.py            # Helper functions for database operations
│
└── tests/                         # Unit and integration tests
    ├── unit/                      # Unit tests for controllers, services, and routers
    │   ├── test_student.py
    │
    └── integration/               # Integration tests (migration, complete data flow)
        ├── test_migration.py
        └── test_student_integration.py

```


## Documentation

All project-related documents are stored in the `docs` folder. This includes:

- [Cahier des Charges](docs/cahier_de_charges.pdf)
- [SQL Database Model](docs/data_model_sql.pdf)
- [NoSQL MongoDB Database Model](docs/migration_sql_to_nosql.md)

You can access these documents for further details about the project requirements and data models.

## Pré-requis

todo