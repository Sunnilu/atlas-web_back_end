from flask import Blueprint, jsonify, abort
from api.v1.auth.basic_auth import BasicAuth

# Create the Blueprint for the views
app_views = Blueprint('app_views', __name__)

# Define the status endpoint
@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """ Simple endpoint to check the status of the API """
    return jsonify({"status": "OK"})

# Define the unauthorized endpoint to test the custom error handler
@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """ Endpoint that triggers a 401 Unauthorized error """
    abort(401)  # This will trigger the custom 401 error handler

# Define the forbidden endpoint to test the custom error handler (optional)
@app_views.route('/api/v1/forbidden', methods=['GET'])
def forbidden_endpoint():
    """ Endpoint that triggers a 403 Forbidden error """
    abort(403)  # This will trigger the custom 403 error handler

# Define a route to simulate authentication error (this can be customized as per your auth logic)
@app_views.route('/api/v1/auth-test', methods=['GET'])
def auth_test():
    """ Endpoint to test if authentication is being handled correctly """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401)  # Raise Unauthorized error if no Authorization header is present
    # Perform authentication checks here (this is just an example)
    # If authentication fails, you could raise 403 or 401 accordingly.
    return jsonify({"message": "Authenticated successfully!"})

