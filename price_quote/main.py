import os, sys

# integrating environment variable through 'dotenv'
from dotenv import load_dotenv

from app import create_flask_app
from config import DevelopmentConfig

app = create_flask_app(DevelopmentConfig)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else: 
    print("No .env file found")
    print("exiting application")
    sys.exit()

if __name__ == '__main__':
    # setup_log()
    app.config.from_object(os.getenv('CONFIGURATION_SETUP'))
    app.run(debug=True, host='0.0.0.0', port=os.getenv('DEV_PORT'))