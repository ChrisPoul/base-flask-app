import click
from flask.cli import AppGroup
from .models import database
from .models.user import User

database_cli = AppGroup('db')


@database_cli.command("init")
def init_database():
    database.drop_all()
    database.create_all()
    click.echo('Initialized Database')


@database_cli.command("drop")
def drop_database():
    database.drop_all()
    click.echo('Droped Database')


@database_cli.command("reset-table")
@click.argument("table_name")
def reset_database_table(table_name):
    click.echo(f'Table "{table_name}" was reset succesfuly')


user_cli = AppGroup('user')


@user_cli.command("create")
@click.argument("name")
def create_user(name: str):
    user = User(name=name)
    user.add()
    click.echo(f'User "{name}" created succesfuly')


@user_cli.command("delete")
@click.argument("name")
def delete_user(name: str):
    user = User.get_by(name=name)
    user.delete()
    click.echo(f'User "{name}" deleted succesfuly')


@user_cli.command("list")
def list_users():
    users = User.all()
    for user in users:
        click.echo(f"username: {user.name}")
