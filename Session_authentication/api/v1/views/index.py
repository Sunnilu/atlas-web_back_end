#!/usr/bin/env python3
"""
Module for status endpoint.
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    GET /api/v1/status
    Returns a simple JSON response to show API is alive.
    """
    return jsonify({"status": "OK"})
