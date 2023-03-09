import os
from flask import Flask


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

    from flask_cors import CORS
    CORS(app)

    from .models import database
    database.init_app(app)

    from .auth import login_manager
    login_manager.init_app(app)

    from .cli import database_cli, user_cli
    app.cli.add_command(database_cli)
    app.cli.add_command(user_cli)

    from .views import bp
    app.register_blueprint(bp)
