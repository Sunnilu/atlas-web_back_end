#!/usr/bin/env python3
"""
Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """GET /api/v1/unauthorized
    This endpoint will raise a 401 Unauthorized error to test the error handler.
    """
    abort(401)  # Trigger the 401 error handler



