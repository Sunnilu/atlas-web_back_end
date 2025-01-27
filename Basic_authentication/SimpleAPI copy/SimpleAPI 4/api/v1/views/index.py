#!/usr/bin/env python3
""" Module of Index views for API version 1
    Provides endpoints to check the status of the API and get statistics of the objects.
"""

from flask import jsonify
from api.v1.views import app_views
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ 
    Endpoint to check the status of the API.
    
    GET /api/v1/status
    
    Return:
      - A JSON response with the status of the API.
      
    Example Response:
      {
        "status": "OK"
      }
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ 
    Endpoint to retrieve statistics about the objects in the system.
    
    GET /api/v1/stats
    
    Return:
      - A JSON response containing the count of each object type (e.g., users).
      
    Example Response:
      {
        "users": 50
      }

    This endpoint can be expanded to include more object types in the future.
    """
    stats = {}
    stats['users'] = User.count()  # Assuming `User.count()` returns the total number of users
    
    return jsonify(stats)
