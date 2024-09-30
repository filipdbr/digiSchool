"""
Sets up MongoDB collections with schema validation.

This script creates the "students" collection with validation rules to ensure data integrity.
It checks if the collection already exists to prevent duplicate creation.

Run during the initial setup to configure MongoDB.
"""

from config.database_nosql import get_mongo_db

# Connect to MongoDB
db = get_mongo_db()

# Define validation schema for students collection
student_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "nom", "prenom", "date_naissance", "sexe"],
        "properties": {
            "_id": {
                "bsonType": "int",
                "description": "must be an integer and is required"
            },
            "nom": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "prenom": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "date_naissance": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "adresse": {
                "bsonType": "string",
                "description": "must be a string"
            },
            "sexe": {
                "enum": ["HOMME", "FEMME"],
                "description": "must be either HOMME or FEMME and is required"
            },
            "classe": {
                "bsonType": "object",
                "properties": {
                    "class_id": {
                        "bsonType": "int",
                        "description": "must be an integer"
                    },
                    "nom": {
                        "bsonType": "string",
                        "description": "must be a string"
                    },
                    "professor": {
                        "bsonType": "object",
                        "properties": {
                            "prof_id": {
                                "bsonType": "int",
                                "description": "must be an integer"
                            },
                            "nom": {
                                "bsonType": "string",
                                "description": "must be a string"
                            },
                            "prenom": {
                                "bsonType": "string",
                                "description": "must be a string"
                            }
                        }
                    }
                }
            },
            "notes": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "note_id": {
                            "bsonType": "int",
                            "description": "must be an integer"
                        },
                        "matiere": {
                            "bsonType": "object",
                            "properties": {
                                "matiere_id": {
                                    "bsonType": "int",
                                    "description": "must be an integer"
                                },
                                "nom": {
                                    "bsonType": "string",
                                    "description": "must be a string"
                                }
                            }
                        },
                        "note": {
                            "bsonType": "int",
                            "description": "must be an integer"
                        },
                        "date_saisie": {
                            "bsonType": "date",
                            "description": "must be a date"
                        },
                        "trimestre": {
                            "bsonType": "object",
                            "properties": {
                                "trimestre_id": {
                                    "bsonType": "int",
                                    "description": "must be an integer"
                                },
                                "nom": {
                                    "bsonType": "string",
                                    "description": "must be a string"
                                }
                            }
                        },
                        "avis": {
                            "bsonType": "string",
                            "description": "must be a string"
                        },
                        "avancement": {
                            "bsonType": "double",
                            "description": "must be a double"
                        }
                    }
                }
            }
        }
    }
}


# Create students collection with validation if it does not already exist
try:
    # Check if the collection already exists
    if "students" not in db.list_collection_names():
        db.create_collection("students", validator={"$jsonSchema": student_validator})
        print("Collection 'students' created successfully")
    else:
        print("Collection 'students' already exists. Skipping creation.")
except Exception as e:
    print(f"Error creating collection: {e}")
