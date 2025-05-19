#!/usr/bin/env python3
"""
Initializer for API view blueprints.
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views
from api.v1.views.users import *
from api.v1.views.index import *
from api.v1.views.session_auth import session_login

# Register session route safely here to avoid circular import
app_views.add_url_rule(
    '/auth_session/login',
    view_func=session_login,
    methods=['POST'],
    strict_slashes=False
)


