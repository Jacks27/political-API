from flask import Flask
from flask import Blueprint
from app.api.v2.models.database import DatabaseConnection
from app.api.v1.views.office_view import my_v1 as office
from app.api.v1.views.party_view import my_v1 as party
from app.api.v1.views.candidate_view import my_v1 as candidates
from app.api.v2.views.users_views import my_v2 as users




from instance.config import app_config


def create_app(config_name):
    """ Application factory """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(party)
    app.register_blueprint(office)
    app.register_blueprint(candidates)
    app.register_blueprint(users)
    db_url =app_config[config_name] .Database_Url
    DatabaseConnection(db_url)
    if config_name == "testing":
        DatabaseConnection.drop_all_tables(DatabaseConnection)
    return app