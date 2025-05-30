#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route():
    """ GET /api/v1/unauthorized """
    abort(401)


# ✅ New test route for 403
@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_route():
    """ GET /api/v1/forbidden """
    abort(403)
