#!/usr/bin/env python3
"""
Main Flask application module for the API.

Handles:
- CORS
- Blueprint registration
- Authentication strategy switch (auth, basic_auth, session_auth)
- Pre-request authentication filtering
- Error handling
"""

from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Authentication strategy initialization
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """
    Runs before each request to enforce authentication.

    Applies to all endpoints except excluded_paths.
    Supports both header-based and session-based authentication.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/users/me',
        '/api/v1/auth_session/login/'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    # Require at least one valid auth method (header or session cookie)
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)

    user = auth.current_user(request)
    if user is None:
        abort(403)

    request.current_user = user


@app.errorhandler(404)
def not_found(error) -> str:
    """Handles 404 Not Found errors."""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Handles 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Handles 403 Forbidden errors."""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
