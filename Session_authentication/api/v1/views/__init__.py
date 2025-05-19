#!/usr/bin/env python3
"""
Initializer for API view blueprints.
"""

from flask import Blueprint
from api.v1.views.session_auth import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all route modules to register them
from api.v1.views.index import *
from api.v1.views.users import *
