#!/usr/bin/env python3
"""Module for managing user-related endpoints."""


from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.views import app_views

# Initialize Flask application
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Authentication configuration
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """
    Hook that runs before each request to handle authentication.
    Sets request.current_user if authentication is successful.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/users/me',
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    user = auth.current_user(request)
    if user is None:
        abort(403)

    request.current_user = user


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handles 401 Unauthorized errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handles 403 Forbidden errors.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
