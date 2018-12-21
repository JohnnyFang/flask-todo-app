from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# local imports
from config import app_config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['production'])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    ma.init_app(app)

    from .webapp import webapp as webapp_blueprint
    app.register_blueprint(webapp_blueprint)

    from .todo_api import todo_api as todo_api_blueprint
    app.register_blueprint(todo_api_blueprint)

    return app

