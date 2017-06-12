import os
from os import getenv

basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = os.getenv('DEBUG', False)
BOT_TOKEN = getenv('BOT_TOKEN')
SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
DB_URI = getenv('DB_URI', 'sqlite:///app.db')
USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'admin')
SECRET_KEY = os.getenv('SECRET_KEY')
