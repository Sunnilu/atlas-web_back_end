#!/usr/bin/env python3
""" Module of Index views
"""
from flask import Flask, jsonify, abort
from api.v1.views import app_views

# Sample imports for other routes and models
from models.user import User

# Route: GET /api/v1/status
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


# Route: GET /api/v1/stats
@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


# Route: GET /api/v1/unauthorized
@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ GET /api/v1/unauthorized
    Return:
      - raises 401 Unauthorized error
    """
    abort(401)


# Custom error handler for 401 Unauthorized
@app_views.errorhandler(401)
def unauthorized_error(error):
    """ Custom handler for 401 Unauthorized error """
    return jsonify({"error": "Unauthorized"}), 401


