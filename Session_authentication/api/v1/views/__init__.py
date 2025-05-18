#!/usr/bin/env python3
"""
Module initializer for views. Registers the API blueprint.
"""

from flask import Blueprint

# Define the blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all routes so they're registered with the blueprint
from api.v1.views.users import *
