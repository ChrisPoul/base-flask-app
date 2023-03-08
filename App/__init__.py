import os
import sys
from flask import Flask
from flask_cors import CORS
from .models import database
from .cli import init_database_command
from .views import bp


def create_app():
    app = Flask(__name__)
    configure_app(app)

    return app


def configure_app(app: Flask):
    app.config.from_pyfile('config.py')
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db_dialect = os.environ.get('DB_DIALECT', default='sqlite')
    db_name = os.environ.get('DB_NAME', default='App_db')
    if db_dialect == 'sqlite':
        app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{app.instance_path}/{db_name}.sqlite'
    CORS(app)

    database.init_app(app)
    app.cli.add_command(init_database_command)
    app.register_blueprint(bp)
