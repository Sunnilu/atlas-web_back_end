#!/usr/bin/env python3
"""
a function that inserts a new document in a collection based on kwargs
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    # Insert the document into the collection with the provided kwargs
    result = mongo_collection.insert_one(kwargs)
    # Return the _id of the new document
    return result.inserted_id
