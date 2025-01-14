# DigiSchool: School Management API with FastAPI, MongoDB, and MariaDB

## Description

This project aims to demonstrate the development of a school management application using FastAPI, MongoDB, and MariaDB. It encompasses features for managing students, professors, classes, and grades. The application also includes data validation with Pydantic, migration from SQL to NoSQL databases, and follows a modular code structure for better maintainability.

## Project Structure

Here is the structure of the project:
```bash
digiSchool
├── docs
│   ├── cahier_de_charges.pdf
│   ├── data_model_sql.png
│   └── migration_sql_to_nosql.md
├── src
│   ├── controllers
│   │   ├── class_controller.py
│   │   ├── grade_controller.py
│   │   ├── professor_controller.py
│   │   ├── student_controller.py
│   │   ├── subject_controller.py
│   │   └── trimester_controller.py
│   ├── migration
│   │   ├── data_migration.py
│   │   └── student_mapper.py
│   ├── models
│   │   ├── base_model.py
│   │   ├── class_model.py
│   │   ├── grade_model.py
│   │   ├── professor_model.py
│   │   ├── student_model.py
│   │   ├── subject_model.py
│   │   └── trimester_model.py
│   ├── routers
│   │   ├── class_router.py
│   │   ├── grade_router.py
│   │   ├── professor_router.py
│   │   ├── student_router.py
│   │   ├── subject_router.py
│   │   └── trimester_router.py
│   ├── schemas
│   │   ├── class_schema.py
│   │   ├── grade_schema.py
│   │   ├── professor_schema.py
│   │   ├── student_schema.py
│   │   ├── subject_schema.py
│   │   └── trimester_schema.py
│   ├── services
│   │   └── professor_service.py
│   ├── utils
│   │   ├── database_nosql.py
│   │   ├── database_sql.py
│   │   ├── env.py
│   │   └── setup_mongodb.py
│   └── main.py
├── tests
├── .env.template
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```
## Documentation

All project-related documents are stored in the `docs` folder. This includes:

- [Cahier des Charges](docs/cahier_de_charges.pdf)
- [SQL Database Model](docs/data_model_sql.pdf)
- [NoSQL MongoDB Database Model](docs/migration_sql_to_nosql.md)

You can access these documents for further details about the project requirements and data models.

## Prerequisites
- Python 3.10 or higher
- Docker (optional, for database management)
- MongoDB and MariaDB
- virtualenv for managing the virtual environment

## Project Installation
1. Clone the project:
```bash
git clone <repository_url>
cd <repository_directory>
```
2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
3. Set up environment variables:
   1. Copy the `.env.template` file and rename it to `.env`
   2. Open the `.env` file and provide the database connection details:

```ini
    MONGODB_URI=mongodb://localhost:27017
    MARIADB_HOST=localhost
    MARIADB_USER=<your_username>
    MARIADB_PASSWORD=<your_password>
    MARIADB_DB=<database_name>
```

## Database Initialization

### MongoDB
When the application starts, MongoDB is automatically initialized. If the `students` collection does not exist yet, it will be created. If it already exists, it will be updated with the new validation rules.

###  Data Migration
On the first run, student data from MariaDB will be automatically migrated to MongoDB. If students already exist in the MongoDB database, they will not be overwritten; only new entries will be added.

## Run the Project

To start the API, run the following command in the terminal at the root of the project:

```bash
python run.py
```
Once the project is running, you can access the interactive documentation of the API automatically generated by FastAPI at the following address:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Authors
**Filip DABROWSKI** et **Marwa BENYAHIA**