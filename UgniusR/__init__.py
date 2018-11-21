from flask import Flask

from UgniusR.api import public_api_bp
from UgniusR.projects import projects_bp
from UgniusR.main import main_bp
from config import Config

# Main objects
app = Flask(__name__)

# Set config
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(public_api_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(main_bp)

