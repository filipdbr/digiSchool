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

## Pré-requis

todo