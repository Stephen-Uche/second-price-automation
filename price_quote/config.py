import os

from pathlib import Path
from dotenv import load_dotenv
from i_config import IConfig

PROJECT_ROOT = str(Path(__file__).parent.parent)
load_dotenv('.env')

db_server = os.environ['DB_SERVER']
db_port = os.environ['DB_PORT']
db_database = os.environ['DB_DATABASE']
db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']

class DevelopmentConfig(IConfig):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True
    PORT = os.environ['DEV_PORT']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'

class ProductionConfig(IConfig):
    ENV = "production"
    DEBUG = False
    PORT = os.environ['PROD_PORT']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_server}:{db_port}/{db_database}'
    SQLALCHEMY_ECHO = False

class DockerConfig(IConfig):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@price-quote-db:{db_port}/{db_database}'
    SQLALCHEMY_ECHO = False

class TestingConfig(IConfig):
    TESTING = True
    PORT = os.environ['DEV_PORT']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_username}:{db_password}@contact-db:{db_port}/{db_database}'
