#!/bin/env python3
'''Python function that lists all documents in a collection'''


def list_all(mongo_collection):
    '''Lists all documents in a collection'''
    cursor = mongo_collection.find()
    return [doc for doc in cursor]