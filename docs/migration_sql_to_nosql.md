# Migration from SQL to NoSQL: Project Documentation

## Overview
This project involves migrating data from a relational SQL database (MariaDB) to a NoSQL database (MongoDB). The goal is to transform the existing SQL model into a more flexible and efficient NoSQL model, which will better serve the application's requirements for CRUD operations. The migration process involves reorganizing data to take advantage of MongoDB's document-based architecture, making data retrieval faster and more intuitive.

## SQL Model Overview
In the current SQL model, data is organized in a normalized fashion across multiple tables to ensure data consistency and reduce redundancy. The key tables include:

- **t_eleve (Student)**: Contains information about students.
- **t_classe (Class)**: Contains information about classes.
- **t_prof (Teacher)**: Contains information about teachers.
- **t_matiere (Subject)**: Contains information about subjects.
- **t_notes (Notes)**: Stores grades given to students for various subjects.
- **t_trimestre (Trimester)**: Contains information about the trimesters.

These tables are linked by foreign keys to maintain data integrity, with relationships defined as follows:
- **Students** (`t_eleve`) are linked to **classes** (`t_classe`) via `classe_id`.
- **Notes** (`t_notes`) are linked to **students**, **teachers**, **subjects**, and **trimesters** via various foreign keys (`ideleve`, `idprof`, `idmatiere`, `idtrimestre`).

In the SQL model, relationships are established using **JOINs** between tables to fetch complete information about entities. This approach, while highly normalized, can result in complex queries and reduced performance for read-heavy applications.

## NoSQL Model Overview
In the NoSQL model, data is reorganized to take full advantage of MongoDB's document-oriented structure. Instead of using normalized tables with foreign keys, related data is embedded within a single document, eliminating the need for multiple JOIN operations.  

The **student document** in MongoDB may contain nested structures that represent class information, grades, and subjects, all in a single document.

##### NoSQL Database Model
```json
{
    "_id": "<student_id>",
    "nom": "<student_name>",
    "prenom": "<student_firstname>",
    "date_naissance": "<date_of_birth>",
    "adresse": "<address>",
    "sexe": "<gender>",
    "classe": {
        "class_id": "<class_id>",
        "nom": "<class_name>",
        "prof": {
            "prof_id": "<teacher_id>",
            "nom": "<teacher_lastname>",
            "prenom": "<teacher_firstname>"
        }
    },
    "notes": [
        {
            "note_id": "<note_id>",
            "matiere": {
                "matiere_id": "<subject_id>",
                "nom": "<subject_name>"
            },
            "note": "<grade_value>",
            "date_saisie": "<date_entered>",
            "trimestre": {
                "trimestre_id": "<trimester_id>",
                "nom": "<trimester_name>"
            },
            "avis": "<comment>",
            "avancement": "<progress>"
        }
    ]
}
```

### Key Changes in the NoSQL Model

1. Denormalization:
    Data that was previously split across multiple tables is now consolidated into a single document.
    For example, information about a student, their class, and the grades they have received are all part of a single document. This structure makes the data easier to read and avoids the need for costly JOIN operations.

2. Embedded Documents:
    Instead of using foreign keys, related data (such as class or teacher details) is stored as embedded documents. This makes retrieving all relevant data for a student straightforward and quick.

3. Redundant Data:
    There is some level of data redundancy (e.g., class and teacher details are repeated in every student document), which is a trade-off for improved read performance. MongoDB's approach favors read-heavy workloads, where data duplication allows for quicker, more efficient reads.

### Differences Between SQL and NoSQL

**1. Data Structure**

- SQL: Data is stored in normalized tables, with different entities (e.g., students, classes, teachers) linked by foreign keys.
- NoSQL (MongoDB): Data is stored in denormalized documents. Each student document includes all necessary related information, reducing the number of queries required to retrieve comprehensive data.

**2. Access Patterns**

- SQL: Requires JOIN operations to gather related data from different tables, which can be computationally expensive.
- NoSQL: Stores related information within a single document, making access to complete data faster, particularly for read-heavy applications.

**3. Flexibility**

- SQL: Schema is strictly defined. Altering the schema requires migrations that can be complex and time-consuming.
- NoSQL: Schema is flexible. Adding new fields or modifying existing documents can be done without a formal schema migration.

### Migration Process

**Step 1: Extract Data from SQL**

Used SQLAlchemy to define models for each table and extract data from the SQL database.
The tables (t_eleve, t_classe, t_prof, etc.) are loaded into Python objects.

**Step 2: Transform Data for MongoDB**

Converted the normalized data from SQL into a denormalized structure suitable for MongoDB.
Combined related data (e.g., students, classes, teachers, and grades) into a single document to optimize for reads.

**Step 3: Load Data into MongoDB**

Used the PyMongo library to insert transformed documents into the MongoDB collection.
Each document is inserted with a unique identifier (_id), and related information is stored in nested structures.

### Why This Organization?
**1. Faster Reads**

By storing all information related to a student in a single document, MongoDB provides faster read times compared to an SQL database that would require multiple JOINs.

**2. Simpler CRUD Operations**

Operations such as creating or updating a student and their related information (e.g., classes, notes) can be handled in one go, rather than interacting with multiple tables.

**3. Scalability**

MongoDB is well-suited for horizontal scaling, meaning that data can be distributed across multiple servers. The denormalized approach supports this by minimizing dependencies between documents.