#!/usr/bin/env python3
"""
Route module for the API.

This module sets up the Flask app, registers the blueprint for the API routes,
and configures Cross-Origin Resource Sharing (CORS). It also handles the 
404 Not Found errors.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS

# Create a Flask application instance
app = Flask(__name__)

# Register the API blueprint to the app
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for the app to allow requests
# from any origin for API routes. CORS is set for the route pattern `/api/v1/*`.
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors globally for the application.

    This function is triggered whenever a route is not found. It returns a 
    JSON response with an error message indicating the resource could not 
    be found.

    Args:
        error: The error object containing information about the 404 error.

    Returns:
        A JSON response with the error message and the HTTP status code 404.

    Example:
        {
            "error": "Not found"
        }
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    """
    Run the Flask application.

    This function runs the app on the specified host and port. The host and 
    port values are retrieved from environment variables, with defaults being 
    "0.0.0.0" for the host and "5000" for the port. If these environment 
    variables are not set, the app will run on the default host and port.

    The app is only run if this script is executed directly (not imported as a module).

    Example:
        $ python3 app.py  # Runs the app on 0.0.0.0:5000
    """
    # Retrieve host and port from environment variables with defaults
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")

    # Start the Flask application
    app.run(host=host, port=int(port))

