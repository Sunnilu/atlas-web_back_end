#!/usr/bin/env python3
"""
Module for handling all routes related to User objects in the API.

Includes the following endpoints:
- GET /api/v1/users
- GET /api/v1/users/<user_id>
- POST /api/v1/users
- PUT /api/v1/users/<user_id>
- DELETE /api/v1/users/<user_id>

Also supports:
- GET /api/v1/users/me to return the authenticated user object.
"""

from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """
    Retrieves the list of all User objects.

    Returns:
        JSON response containing a list of all users.
    """
    users = User.all()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves a User object by ID or the authenticated user if user_id is 'me'.

    Args:
        user_id (str): The user ID or 'me'.

    Returns:
        JSON response containing the user's data, or 404 if not found.
    """
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
    """
    Creates a new User object using request data.

    Returns:
        JSON response with the created user's data, or 400 error.
    """
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
    """
    Updates an existing User object with new data.

    Args:
        user_id (str): The ID of the user to update.

    Returns:
        JSON response with the updated user's data, or error.
    """
    user = User.get(user_id)
    if user is None:
        abort(404)

    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    data = request.get_json()
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a User object by ID.

    Args:
        user_id (str): The ID of the user to delete.

    Returns:
        Empty JSON response with 200 status, or 404 if not found.
    """
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200
