#!/usr/bin/env python3
"""
Session authentication view module.
Handles login via session mechanism.
"""

from flask import request, jsonify, make_response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    POST /api/v1/auth_session/login
    Handles session-based login using email and password.

    Returns:
        JSON response with user data or appropriate error messages.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # Step 1: Validate email
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Step 2: Validate password
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Step 3: Find user by email
    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Step 4: Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Step 5: Create session ID and set cookie
    from api.v1.app import auth  # import here to avoid circular import

    session_id = auth.create_session(user.id)
    if session_id is None:
        return jsonify({"error": "session creation failed"}), 500

    response = make_response(user.to_json())
    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
