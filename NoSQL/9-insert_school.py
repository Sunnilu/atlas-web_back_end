#!/usr/bin/env python3
"""
This script contains a function to insert a new school document into a MongoDB collection.

Function:
    - insert_school: Inserts a new document into the specified MongoDB collection
      using keyword arguments and returns the generated _id.

Requirements:
    - pymongo library: Ensure you have pymongo installed.
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new school document into the given MongoDB collection.

    Parameters:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object
        **kwargs: The fields and values to be inserted into the document.

    Returns:
        str: The _id of the newly inserted document.
    """
    # Insert the document using the keyword arguments provided
    result = mongo_collection.insert_one(kwargs)
    # Return the _id of the newly inserted document
    return result.inserted_id
