from flask import Flask
from api.v1.views import app_views

app = Flask(__name__)

# Register the Blueprint for views
app.register_blueprint(app_views, url_prefix='/api/v1')

# Add additional configurations, error handlers, etc.
