#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views  # Make sure this import matches your app's structure
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, jsonify, abort, request
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)

# Register blueprint for views
app.register_blueprint(app_views)

# Enable CORS for the API
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize authentication handling based on environment variable
auth = None
if getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handle 404 errors
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handle 401 Unauthorized errors
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handle 403 Forbidden errors
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """
    Check for required authorization before processing the request
    """
    authorized_list = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    # If authentication is required, check authorization headers
    if auth and auth.require_auth(request.path, authorized_list):
        if not auth.authorization_header(request):
            abort(401)  # Unauthorized if no authorization header
        if not auth.current_user(request):
            abort(403)  # Forbidden if no valid user is found


if __name__ == "__main__":
    # Set host and port from environment variables or use defaults
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    
    # Run the app on the specified host and port
    app.run(host=host, port=port)
