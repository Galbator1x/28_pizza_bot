import os
from os import getenv

basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = os.getenv('DEBUG', False)
BOT_TOKEN = getenv('BOT_TOKEN')
SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI',
                                 'sqlite:///' + os.path.join(basedir, 'app.db'))
USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'admin')
