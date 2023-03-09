import os
from typing import Mapping, Union
from flask import Flask


def create_app(test_config: Union[Mapping, None] = None):
    app = Flask(__name__)
    _configure_app(app, test_config)

    return app


def _configure_app(app: Flask, test_config: Union[Mapping, None] = None):
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py')
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db_dialect = os.environ.get('DB_DIALECT', default='sqlite')
    db_name = os.environ.get('DB_NAME', default='App_db')
    if db_dialect == 'sqlite':
        app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{app.instance_path}/{db_name}.sqlite'

    from flask_cors import CORS
    CORS(app)

    from .models import database
    database.init_app(app)

    from .auth import login_manager
    login_manager.init_app(app)

    _configure_cli(app)
    _configure_blueprints(app)


def _configure_cli(app: Flask):
    from .cli import database_cli, user_cli
    app.cli.add_command(database_cli)
    app.cli.add_command(user_cli)


def _configure_blueprints(app: Flask):
    from .views import home_bp
    app.register_blueprint(home_bp)
    from .views.auth import auth_bp
    app.register_blueprint(auth_bp)
