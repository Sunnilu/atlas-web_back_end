# api/v1/views/__init__.py

from flask import Blueprint

# Define the Blueprint object for app_views
app_views = Blueprint('app_views', __name__)

# Avoid circular imports by only importing views *after* the Blueprint is defined
# Import specific view modules after app_views is set up
from api.v1.views import some_view_module  # Import specific view modules
