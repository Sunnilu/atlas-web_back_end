#!/usr/bin/env python3
'''Python function that lists all documents in a collection'''


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: A PyMongo collection object
    
    Returns:
        list: A list of all documents in the collection. Returns empty list if no documents exist.
    """
    try:
        # Use find() to get a cursor for all documents
        cursor = mongo_collection.find()
        
        # Convert the cursor to a list
        # This will return an empty list if no documents exist
        return list(cursor)
    except Exception as e:
        # Log the error and return an empty list
        print(f"An error occurred: {str(e)}")
        return []