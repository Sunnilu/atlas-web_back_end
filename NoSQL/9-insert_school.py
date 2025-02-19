#!/usr/bin/env python3
"""
Insert a new school document into the collection and return its _id.
"""

from pymongo import MongoClient


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
