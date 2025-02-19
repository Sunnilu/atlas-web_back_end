#!/usr/bin/env python3
"""MongoDB school database operations module"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
 