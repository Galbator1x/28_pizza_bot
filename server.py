from models import Pizza, PizzaChoices

import os

from flask import Flask, abort, request, Response, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
session = Session(engine)


def check_auth(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class PizzaModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True

    inline_models = (PizzaChoices,)


admin = Admin(app, name='menu', template_mode='bootstrap3')
admin.add_view(PizzaModelView(Pizza, session))


if __name__  ==  '__main__':
    app.run()
