import os
from abc import ABCMeta

class IConfig(metaclass=ABCMeta):
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	BUNDLE_ERRORS = True
	USE_CORS = True
	APP_DIR = os.path.abspath(os.path.dirname(__file__))
	PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
 