#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os


# Create the Flask app
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for the API
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Custom error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


# Custom error handler for 401 - Unauthorized
@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


# Main entry point for the Flask app
if __name__ == "__main__":
    # Get host and port from environment variables (or use defaults)
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    
    # Run the app
    app.run(host=host, port=port)
