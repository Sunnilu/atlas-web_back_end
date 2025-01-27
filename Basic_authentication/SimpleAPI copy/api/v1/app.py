# Import jsonify from Flask
from flask import jsonify, abort, request

# Existing error handler for 404
@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

# Add a new error handler for 401 status code
@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401

# Existing code...

# Testing the new error handler
from api.v1.views import index  # Assuming index.py is in the same directory as api/v1/views/__init__.py

@index.route("/api/v1/unauthorized")
def unauthorized_endpoint():
    abort(401)  # Raise a 401 error to trigger the custom error handler
    return "This line will not be executed"  # This line is unreachable because abort raises an exception