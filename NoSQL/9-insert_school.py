#!/usr/bin/env python3
'''Inserts a new document into a MongoDB collection'''


from pymongo import MongoClient
import sys

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.
    
    Args:
        mongo_collection: A PyMongo collection object
        **kwargs: Key-value pairs to be inserted as document fields
    
    Returns:
        ObjectId: The _id of the newly inserted document
    """
    try:
        # Insert the document and get the inserted_id
        result = mongo_collection.insert_one(kwargs)
        
        # Return the _id of the newly inserted document
        return result.inserted_id
    except Exception as e:
        # Log the error and re-raise it
        print(f"An error occurred: {str(e)}")
        raise

def main():
    # Create a client and connect to the database
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_db
    school_collection = db.school
    
    # Test 1: Empty collection - create one simple document
    print("\nTest 1: Empty collection - create one simple document")
    simple_doc = {"name": "Test School 1", "address": "123 Main St"}
    new_id = insert_school(school_collection, **simple_doc)
    print(f"Inserted document with ID: {new_id}")
    
    # Test 2: Collection with 1 document - create one simple document
    print("\nTest 2: Collection with 1 document - create one simple document")
    simple_doc = {"name": "Test School 2", "address": "456 Oak Ave"}
    new_id = insert_school(school_collection, **simple_doc)
    print(f"Inserted document with ID: {new_id}")
    
    # Test 3: Collection with 5 documents - create one simple document
    print("\nTest 3: Collection with 5 documents - create one simple document")
    simple_doc = {"name": "Test School 3", "address": "789 Pine Rd"}
    new_id = insert_school(school_collection, **simple_doc)
    print(f"Inserted document with ID: {new_id}")
    
    # Test 4: Collection with 5 documents - create 5 simple documents
    print("\nTest 4: Collection with 5 documents - create 5 simple documents")
    simple_docs = [
        {"name": f"Test School {i}", "address": f"{i*100} Maple St"}
        for i in range(4, 9)
    ]
    for doc in simple_docs:
        new_id = insert_school(school_collection, **doc)
        print(f"Inserted document with ID: {new_id}")
    
    # Test 5: Collection with 5 documents - create 1 complex document
    print("\nTest 5: Collection with 5 documents - create 1 complex document")
    complex_doc = {
        "name": "Complex School",
        "address": "Complex Ave",
        "departments": ["Math", "Science", "History"],
        "teachers": [
            {"name": "John", "subject": "Math"},
            {"name": "Jane", "subject": "Science"}
        ],
        "metadata": {
            "founded": 2000,
            "capacity": 1000,
            "rating": 4.5
        }
    }
    new_id = insert_school(school_collection, **complex_doc)
    print(f"Inserted document with ID: {new_id}")
    
    # Test 6: Collection with 5 documents - create 5 complex documents
    print("\nTest 6: Collection with 5 documents - create 5 complex documents")
    complex_docs = [
        {
            "name": f"Complex School {i}",
            "address": f"Complex Ave {i}",
            "departments": ["Math", "Science", "History"],
            "teachers": [
                {"name": f"Teacher {i*2}", "subject": "Math"},
                {"name": f"Teacher {i*2+1}", "subject": "Science"}
            ],
            "metadata": {
                "founded": 2000 + i,
                "capacity": 1000 + i*100,
                "rating": 4.5 + i*0.1
            }
        }
        for i in range(1, 6)
    ]
    for doc in complex_docs:
        new_id = insert_school(school_collection, **doc)
        print(f"Inserted document with ID: {new_id}")

if __name__ == "__main__":
    main()