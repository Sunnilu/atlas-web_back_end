#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os


def create_app() -> Flask:
    """
    Creates and configures the Flask application instance.
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    app.register_blueprint(app_views)
    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    auth = None
    if os.getenv('AUTH_TYPE') == 'auth':
        from api.v1.auth.auth import Auth
        auth = Auth()
    elif os.getenv('AUTH_TYPE') == "basic_auth":
        from api.v1.auth.basic_auth import basic_auth
        auth = BasicAuth()

    @app.errorhandler(403)
    def forbidden(error) -> str:
        '''Request forbidden'''
        return jsonify({"error": "Forbidden"}), 403
    
    @app.errorhandler(404)
    def not_found(error) -> str:
        '''Handles 404 Not Found errors'''
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(401)
    def unauthorized(error) -> str:
        '''Handles 401 Unauthorized errors'''
    
        return jsonify({"error": "Unauthorized"}), 401

    @app.before_request
def before_request():
    """ Before request
    """
    if auth and auth.require_auth(request.path, ['/api/v1/status/',
                                                 '/api/v1/unauthorized/',
                                                 '/api/v1/forbidden/']):
        if not auth.authorization_header(request):
            abort(401)
        if not auth.current_user(request):
            abort(403)
            

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app = create_app()
    app.run(host=host, port=port)
