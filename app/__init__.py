from config import Config
from flask import Flask

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

from app import routes