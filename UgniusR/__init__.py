import os
from dotenv import load_dotenv
from flask import Flask, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from UgniusR.api import public_api_bp
from UgniusR.projects import projects_bp
from UgniusR.main import main_bp
from config import Config

# Main objects
app = Flask(__name__)

# Load environment variables
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Set up Sentry
if 'SENTRY_DSN' in os.environ:
    SENTRY_DSN = os.environ['SENTRY_DSN']
    sentry_sdk.init(SENTRY_DSN, integrations=[FlaskIntegration()], environment=os.environ['ENVIRONMENT'])

# Set config
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(public_api_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(main_bp)

