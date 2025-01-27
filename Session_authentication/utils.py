#!/usr/bin/env python3

# utils.py
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "Unauthorized"}), 401
    
    return app
