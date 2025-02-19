#!/usr/bin/env python3
'''Returns a list of schools having a specific topic'''

import pymongo

def schools_by_topic(mongo_collection, topic):
    '''
    Returns a list of school documents that have the specified topic in their topics field.

    Parameters:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents that contain the specified topic.
    '''
    # Query to find schools that have the topic in their 'topics' list
    return mongo_collection.find({'topics': topic})
