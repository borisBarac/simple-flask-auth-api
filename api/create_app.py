import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY') or ''

def create_app(__name__):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.url_map.strict_slashes = False
    return app