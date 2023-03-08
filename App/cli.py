import click
from flask.cli import with_appcontext
from .models import database


def init_database():
    database.drop_all()
    database.create_all()


@click.command('init-db')
@with_appcontext
def init_database_command():
    init_database()
    click.echo('Initialized Database')
