#!/usr/bin/env python3
"""
Main module for the API
"""

from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

# Initialize the Flask app
app = Flask(__name__)

# Register the Blueprint for views
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for all routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize authentication mechanism (either BasicAuth or Auth)
auth = None
if getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()

# Error handler for 404 (Not Found)
@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404

# Error handler for 401 (Unauthorized)
@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401

# Error handler for 403 (Forbidden)
@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403

# This function is executed before every request to handle authentication
@app.before_request
def before_request():
    """
    Handler before each request.
    Checks if the request requires authentication and if so, verifies the current user.
    """
    authorized_list = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    # Check if authentication is required for this route
    if auth and auth.require_auth(request.path, authorized_list):
        if not auth.authorization_header(request):
            abort(401)  # Unauthorized if no authorization header
        if not auth.current_user(request):
            abort(403)  # Forbidden if no valid user found
        
        # Assign the current user to the request object
        request.current_user = auth.current_user(request)

# Main entry point of the Flask app
if __name__ == "__main__":
    # Get host and port from environment variables, default to '0.0.0.0' and '5000'
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    # Run the Flask app
    app.run(host=host, port=port, debug=True)
