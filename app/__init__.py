from flask import Flask
from flask import Blueprint
from app.api.v1.views.party_view import my_v1 as v1


# from instance.config import DevConfig


def create_app():
    app = Flask(__name__)
    # app.config.from_object(DevConfig[config_name])
    # app.config.from_pyfile('config.py')
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app