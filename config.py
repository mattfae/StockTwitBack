"""Flask configuration"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    FLASK_APP = 'wsgi.py'
    SECRET_KEY = environ.get('SECRET_KEY')
    #SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    #STATIC_FOLDER = 'static'
    #TEMPLATES_FOLDER = 'templates'
    MONGODB_SETTINGS = {
    'db': 'bricktime',
    'host': 'mongodb://127.0.0.1:27017/bricktime'
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