from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '14f9d68685b8c04a6e4e5088'

from routes.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)