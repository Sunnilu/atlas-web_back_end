#!/usr/bin/env python3
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