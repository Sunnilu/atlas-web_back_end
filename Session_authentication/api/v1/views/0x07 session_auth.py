#!/usr/bin/env python3
"""
Session authentication view module.
Defines the login logic, but route is registered in __init__.py.
"""

from flask import request, jsonify, make_response
from models.user import User
import os


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

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth  # avoid circular import
    session_id = auth.create_session(user.id)

    response = make_response(user.to_json())
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
