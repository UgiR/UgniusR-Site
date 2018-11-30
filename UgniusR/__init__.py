from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config
from UgniusR.api import public_api_bp
from UgniusR.projects import projects_bp
from UgniusR.main import main_bp

# Main objects
app = Flask(__name__)
app.config.from_object(Config)

# Set up Sentry error reporting
sentry_sdk.init(app.config['SENTRY_DSN'], integrations=[FlaskIntegration()], environment=app.config['ENVIRONMENT'])

# Register blueprints
app.register_blueprint(public_api_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(main_bp)
