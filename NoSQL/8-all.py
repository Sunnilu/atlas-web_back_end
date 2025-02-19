#!/usr/bin/env python3
"""
List all documents in a collection.
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection. If the collection is empty, returns an empty list.
    """
    return list(mongo_collection.find())
