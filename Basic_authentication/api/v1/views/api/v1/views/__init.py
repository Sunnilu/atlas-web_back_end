from flask import Blueprint

# Create a Blueprint for the views
app_views = Blueprint('app_views', __name__)

# Import the views after the Blueprint is created to avoid circular imports
from api.v1.views.index import *
