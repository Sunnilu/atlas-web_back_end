#!/usr/bin/env python3
"""
Initializer for API view blueprints.
Registers all route modules for the API.
"""

from flask import Blueprint

# Create the blueprint with API prefix
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views to register their routes
from api.v1.views.index import *
from api.v1.views.users import *

# Import login and logout view functions (not app_views to avoid circular import)
from api.v1.views.session_auth import session_login, session_logout

# Register login route explicitly
app_views.add_url_rule(
    '/auth_session/login',
    view_func=session_login,
    methods=['POST'],
    strict_slashes=False
)

# ✅ Register logout route explicitly
app_views.add_url_rule(
    '/auth_session/logout',
    view_func=session_logout,
    methods=['DELETE'],
    strict_slashes=False
)

