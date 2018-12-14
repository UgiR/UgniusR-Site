from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from config import Config

# Main objects
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up Sentry error reporting
sentry_sdk.init(app.config['SENTRY_DSN'], integrations=[FlaskIntegration()], environment=app.config['ENV'])

# Register blueprints
from UgniusR.api import public_api_bp
from UgniusR.projects import projects_bp
from UgniusR.main import main_bp
app.register_blueprint(public_api_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(main_bp)

from UgniusR.api import models
