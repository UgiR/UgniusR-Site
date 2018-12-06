import os
import sys
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Load environment variables
    load_dotenv(os.path.join(basedir, '.env'))

    try:

        ENVIRONMENT = os.environ['ENVIRONMENT']

        SENTRY_DSN = os.environ['SENTRY_DSN']

        SECRET_KEY = os.environ['SECRET_KEY']

    except KeyError as e:
        print('Error when loading environment variable \'' + e + '\'')
        sys.exit(1)
