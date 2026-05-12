from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

bcrypt = Bcrypt(app)

from routes.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)