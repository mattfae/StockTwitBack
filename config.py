"""Flask configuration"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    FLASK_APP = 'wsgi.py'
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    CONSUMER_SECRET_KEY = environ.get('CONSUMER_SECRET_KEY')
    MONGODB_SETTINGS = {
    'db': 'bricktime',
    'host': 'mongodb://127.0.0.1:27017/stocktwit'
    }

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    