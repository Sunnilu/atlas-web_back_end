#!/usr/bin/env python3
"""
a function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new school document into the collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The fields and values for the new school document.

    Returns:
        The _id of the newly inserted school document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
