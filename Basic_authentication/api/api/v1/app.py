#!/usr/bin/env python3
"""
Route module for the API

This module sets up the Flask application, configures error handlers, 
and defines the routes for the API. It also handles dynamic authentication 
configuration based on an environment variable.

Key features:
- The app uses BasicAuth or a default Auth class based on the environment variable `AUTH_TYPE`.
- Includes error handlers for 404 (Not Found) and 401 (Unauthorized) errors.
- CORS is enabled for the API, allowing all origins.

Dependencies:
- Flask: A micro web framework for Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import os

# Conditional import of authentication classes based on the environment variable `AUTH_TYPE`
auth = None
if getenv("AUTH_TYPE") == "basic_auth":
    # If AUTH_TYPE is set to "basic_auth", import and use the BasicAuth class
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    # Default to using the Auth class from api.v1.auth.auth
    from api.v1.auth.auth import Auth  
    auth = Auth()

# Initialize Flask application
app = Flask(__name__)

# Register the app_views blueprint (handles the main API routes)
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for the app on routes under /api/v1/*
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(error) -> str:
    """
    404 Error handler for "Not Found" errors.

    This function is triggered whenever a route is requested that doesn't exist in the application.
    
    Args:
        error: The error object representing the 404 error.

    Returns:
        A JSON response with an error message and the status code 404.
    
    Example:
        Response: {"error": "Not found"} with a 404 status code.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    401 Error handler for "Unauthorized" errors.

    This function is triggered when a request fails due to lack of proper authentication 
    or authorization. It returns a standardized error response for unauthorized requests.
    
    Args:
        error: The error object representing the 401 error.

    Returns:
        A JSON response with an error message and the status code 401.
    
    Example:
        Response: {"error": "Unauthorized"} with a 401 status code.
    """
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    # Retrieve host and port configuration from environment variables, defaulting to '0.0.0.0' and '5000'
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")

    # Start the Flask app with the specified host and port
    app.run(host=host, port=port)

