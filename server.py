from models import db, Pizza, PizzaChoices

import os

from flask import Flask, abort, request, Response, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(24)
db.init_app(app)


def check_auth(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']


def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


class PizzaModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization
        if not auth:
            return False
        return check_auth(auth.username, auth.password)

    def inaccessible_callback(self, name, **kwargs):
        return authenticate()

    inline_models = (PizzaChoices,)


admin = Admin(app, name='menu', template_mode='bootstrap3')
admin.add_view(PizzaModelView(Pizza, db.session))


if __name__  ==  '__main__':
    app.run()
