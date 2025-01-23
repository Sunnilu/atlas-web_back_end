# api/v1/views/__init__.py

from flask import Blueprint

# Define the Blueprint object for app_views
app_views = Blueprint('app_views', __name__)

# Import views (routes) that will be registered to this blueprint
from api.v1.views import some_view_module  # Import specific view modules
