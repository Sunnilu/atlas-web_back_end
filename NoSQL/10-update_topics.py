#!/usr/bin/env python3
'''Changes all topics of a school document based on the name'''

import pymongo

def update_topics(mongo_collection, name, topics):
    '''
    Updates the topics of all school documents that match the provided name.

    Parameters:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school document(s) to update.
        topics (list): The list of topics to set in the document.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation, including
                                      the number of documents modified.
    '''
    # Update all documents where the name matches the provided value
    result = mongo_collection.update_many(
        {'name': name},  # Query to match documents by name
        {'$set': {'topics': topics}}  # Update the 'topics' field
    )
    return result
