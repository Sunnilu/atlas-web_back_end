#!/usr/bin/env python3
"""
Module of Index views

This module contains routes and error handlers for the API.
Specifically, it includes an endpoint that triggers a 401 Unauthorized error
for testing purposes.
"""
from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """
    GET /api/v1/unauthorized

    This endpoint is used to simulate and raise a 401 Unauthorized error.
    It can be used for testing the error handler for unauthorized access.
    When this endpoint is accessed, it triggers the abort() function
    with a 401 status code, which will be handled by a custom error handler
    if defined.

    Returns:
        None: This function raises a 401 Unauthorized error, no response is returned.

    Example:
        GET /api/v1/unauthorized
        Response: 401 Unauthorized
    """
    abort(401)  # Trigger the 401 Unauthorized error handler




