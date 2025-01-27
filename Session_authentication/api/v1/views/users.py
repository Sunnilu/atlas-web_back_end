#!/usr/bin/env python3
''' Users module'''


from flask import Blueprint, jsonify, abort, request
from models import User  # Assuming you have a User model that can fetch a user by user_id
from api.v1.auth.basic_auth import BasicAuth

# Define the Blueprint for users
app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """ Retrieves a user by user_id or returns the authenticated user if user_id is 'me' """
    
    # If the user_id is 'me', return the authenticated user
    if user_id == 'me':
        if request.current_user is None:
            abort(404)  # If the current_user is None, it means the user is not authenticated
        return jsonify(request.current_user.to_dict())  # Return the authenticated user details
    
    # Otherwise, fetch the user by user_id
    user = User.get(user_id)  # Replace with your logic to fetch a user by user_id
    if user is None:
        abort(404)  # Return 404 if the user was not found
    return jsonify(user.to_dict())  # Return user details if found


