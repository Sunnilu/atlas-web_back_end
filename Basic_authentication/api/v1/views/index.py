#!/usr/bin/env python3
""" Module of Index views
This module contains the views (routes) for the index of the API. It handles several routes,
including the status of the API, statistics about objects, and tests for unauthorized and forbidden
access. This file uses Flask's route decorators to define the endpoints and their behavior.
"""

from flask import jsonify, abort
from api.v1.views import app_views

# Route: /status
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ 
    GET /api/v1/status
    Endpoint to check the status of the API.

    Returns:
      - A JSON object indicating the status of the API with a key "status" and value "OK".
    """
    return jsonify({"status": "OK"})


# Route: /stats
@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ 
    GET /api/v1/stats
    Endpoint to retrieve the number of objects in the system.

    This endpoint counts the number of users in the database and returns the count as part of a
    JSON object.

    Returns:
      - A JSON object with a key for each type of object (e.g., 'users'), where the value is the count of the objects.
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()  # Count the number of users
    return jsonify(stats)


# Route: /unauthorized
@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ 
    GET /api/v1/unauthorized
    Endpoint that forces the client to receive a 401 Unauthorized error.

    This endpoint calls Flask's abort function with a 401 status code, which triggers an error
    handler elsewhere in the application (such as a global error handler).

    Returns:
      - None (It raises an error, which will result in a 401 Unauthorized response).
    """
    abort(401)


# Route: /forbidden
@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ 
    GET /api/v1/forbidden
    Endpoint that forces the client to receive a 403 Forbidden error.

    This endpoint calls Flask's abort function with a 403 status code, which triggers an error
    handler elsewhere in the application (such as a global error handler).

    Returns:
      - None (It raises an error, which will result in a 403 Forbidden response).
    """
    abort(403)
