import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Load environment variables
load_dotenv(os.path.join(basedir, '.env'))


class Config:

    ENVIRONMENT = os.environ['ENVIRONMENT']

    SENTRY_DSN = os.environ['SENTRY_DSN']

    SECRET_KEY = os.environ['SECRET_KEY']
