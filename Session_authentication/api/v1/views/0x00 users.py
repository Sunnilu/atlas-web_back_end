#!/usr/bin/env python3
"""
User view for handling User-related endpoints
"""
from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """GET /api/v1/users - List all users"""
    users = User.all()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """GET /api/v1/users/<user_id> - Retrieve a user by ID or 'me'"""
    if user_id == "me":
        if not hasattr(request, "current_user") or request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """POST /api/v1/users - Create a new user"""
    from api.v1.app import auth

    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    data = request.get_json()
    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    if 'password' not in data:
        return jsonify({"error": "Missing password"}), 400

    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """PUT /api/v1/users/<user_id> - Update user attributes"""
    user = User.get(user_id)
    if user is None:
        abort(404)

    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    data = request.get_json()
    ignore = ['id', 'email', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """DELETE /api/v1/users/<user_id> - Delete a user"""
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200
