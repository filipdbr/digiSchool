"""
Sets up MongoDB collections with schema validation.

This script creates the "students" collection with validation rules to ensure data integrity.
It checks if the collection already exists to prevent duplicate creation.

Run during the initial setup to configure MongoDB.
"""

from utils.database_nosql import get_db_nosql

# Connect to MongoDB
db = get_db_nosql()

# Define validation schema for students collection
student_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["student_id", "last_name", "first_name", "date_of_birth", "gender"],
        "properties": {
            "student_id": {
                "bsonType": "int",
                "description": "must be an integer and is required"
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "first_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "date_of_birth": {
                "bsonType": "string",
                "description": "must be a date and is required"
            },
            "address": {
                "bsonType": "string",
                "description": "must be a string"
            },
            "gender": {
                "enum": ["HOMME", "FEMME"],
                "description": "must be either HOMME or FEMME and is required"
            },
            "student_class": {
                "bsonType": "object",
                "properties": {
                    "class_id": {
                        "bsonType": "int",
                        "description": "must be an integer"
                    },
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string"
                    },
                    "professor": {
                        "bsonType": "object",
                        "properties": {
                            "professor_id": {
                                "bsonType": "int",
                                "description": "must be an integer"
                            },
                            "last_name": {
                                "bsonType": "string",
                                "description": "must be a string"
                            },
                            "first_name": {
                                "bsonType": "string",
                                "description": "must be a string"
                            },
                            "date_of_birth": {
                                "bsonType": "string",
                                "description": "must be a date and is required"
                            },
                            "address": {
                                "bsonType": "string",
                                "description": "must be a string"
                            },
                            "gender": {
                                "enum": ["HOMME", "FEMME"],
                                "description": "must be either HOMME or FEMME and is required"
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
                        "grade_id": {
                            "bsonType": "int",
                            "description": "must be an integer"
                        },
                        "subject": {
                            "bsonType": "object",
                            "properties": {
                                "subject_id": {
                                    "bsonType": "int",
                                    "description": "must be an integer"
                                },
                                "name": {
                                    "bsonType": "string",
                                    "description": "must be a string"
                                }
                            }
                        },
                        "grade_value": {
                            "bsonType": "int",
                            "description": "must be an integer"
                        },
                        "date_entered": {
                            "bsonType": "string",
                            "description": "must be a date"
                        },
                        "trimester": {
                            "bsonType": "object",
                            "properties": {
                                "trimester_id": {
                                    "bsonType": "int",
                                    "description": "must be an integer"
                                },
                                "name": {
                                    "bsonType": "string",
                                    "description": "must be a string"
                                }
                            }
                        },
                        "comment": {
                            "bsonType": "string",
                            "description": "must be a string"
                        },
                        "progress": {
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
        db.create_collection(
            "students",
            validator={
                "$jsonSchema": student_validator["$jsonSchema"]  # Access the $jsonSchema from the validator dictionary
            }
        )
        print("Collection 'students' created successfully")
    else:
        print("Collection 'students' already exists. Skipping creation.")
except Exception as e:
    print(f"Error creating collection: {e}")