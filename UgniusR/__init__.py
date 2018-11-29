import os
import sys
from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from UgniusR.api import public_api_bp
from UgniusR.projects import projects_bp
from UgniusR.main import main_bp
from config import Config

if 'SENTRY_DSN' not in os.environ:
    sys.exit(1)

SENTRY_DSN = os.environ.get('SENTRY_DSN')
sentry_sdk.init(SENTRY_DSN, integrations=[FlaskIntegration()])

# Main objects
app = Flask(__name__)

# Set config
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(public_api_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(main_bp)

