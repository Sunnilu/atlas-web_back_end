#!/usr/bin/env python3
""" Module of Index views
This module contains the views (routes) for the main API endpoints such as:
- /status: Returns the status of the API.
- /stats: Returns the number of objects in the system (e.g., users).
- /unauthorized: Aborts with a 401 Unauthorized status.
- /forbidden: Aborts with a 403 Forbidden status.
"""

from flask import jsonify, abort
from api.v1.views import app_views
from flask import Blueprint, jsonify, abort


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/status
    Returns the status of the API.
    
    This route is used to check if the API is running and responsive.
    It doesn't require authentication.

    Returns:
        JSON response with the status message.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats
    Returns the number of each object in the system.
    
    This route provides a summary of the total number of objects in the system,
    like the total number of users. It uses the `User.count()` method to get the count.
    
    Returns:
        JSON response with statistics, for example the count of users.
    """
    from models.user import User  # Import the User model from the models directory
    stats = {}
    stats['users'] = User.count()  # Assuming count() returns the number of users
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - Aborts with 401 Unauthorized status and JSON response
    """
    abort(401)  # Flask will automatically set the response Content-Type to application/json



@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """
    GET /api/v1/forbidden
    Triggers a 403 Forbidden error.
    
    This route is used to simulate a Forbidden access error. It is typically
    used to test the behavior of the application when the user tries to access a resource
    they are not allowed to view.

    Raises:
        HTTPException (403): This will trigger a 403 Forbidden error.

    Returns:
        None: The route directly triggers an error (abort(403)).
    """
    abort(403)  # Immediately aborts the request with a 403 Forbidden status

    app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """
    A simple status endpoint that returns a JSON response
    with a status key and value of 'OK'.
    """
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """
    Endpoint to test Unauthorized (401) error handler.
    This will trigger a 401 error and invoke the error handler.
    """
    abort(401)  # This triggers the 401 Unauthorized error handler