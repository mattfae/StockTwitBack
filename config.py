"""Flask configuration"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    FLASK_APP = 'wsgi.py'
    MONGODB_SETTINGS = {
    'db': 'stocktwit',
    'host': 'mongodb://127.0.0.1:27017/stocktwit'
    }


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    