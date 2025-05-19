#!/usr/bin/env python3
"""
Session authentication view module.
Handles login via session mechanism.
"""

from flask import request, jsonify, make_response
from models.user import User
import os
from api.v1.views import app_views  # ✅ Safe to import — used *after* all view logic


def session_login():
    """
    POST /api/v1/auth_session/login
    Handles session-based login using email and password.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth  # ✅ Only imported when needed
    session_id = auth.create_session(user.id)
    if session_id is None:
        return jsonify({"error": "session creation failed"}), 500

    response = make_response(user.to_json())
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response


# ✅ Register the route AFTER everything is defined
app_views.add_url_rule(
    '/auth_session/login',
    view_func=session_login,
    methods=['POST'],
    strict_slashes=False
)
