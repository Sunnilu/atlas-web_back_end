#!/usr/bin/env python3
'''Provides stats about Nginx logs stored in MongoDB'''

from pymongo import MongoClient

def log_stats():
    '''
    Logs statistics from Nginx logs stored in MongoDB.
    
    This function connects to a MongoDB database, queries the logs collection,
    and prints the following statistics:
    1. The total number of logs.
    2. The count of each HTTP method (GET, POST, PUT, PATCH, DELETE).
    3. The count of GET requests with path '/status'.
    
    No parameters or return values.
    '''
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # The database 'logs'
    collection = db.nginx  # The collection 'nginx'
    
    # Count the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Methods: GET, POST, PUT, PATCH, DELETE
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    
    # Count the number of GET requests with path = /status
    status_check = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
