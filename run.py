from flask import Flask
import os
from dotenv import load_dotenv
from extensions import bcrypt, login_manager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from routes.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)