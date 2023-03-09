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
@click.option("--name")
def create_user(name: str):
    user = User(name=name)
    user.add()
    click.echo(f'User "{name}" created succesfuly')


@user_cli.command("delete")
@click.option("--id")
@click.option("--name")
def delete_user(id: str, name: str):
    if id:
        user = User.get(id)
    else:
        user = User.get_by(name=name)
    if user:
        user.delete()
        click.echo(f'User "{name}" deleted succesfuly')
    else:
        click.echo("No user found")


@user_cli.command("list")
def list_users():
    users = User.all()
    for user in users:
        click.echo(f"username: {user.name}")


@user_cli.command("get")
@click.option("--id")
@click.option("--name")
def get_user(id: str, name: str):
    if id:
        user = User.get(id)
    else:
        user = User.get_by(name=name)
    click.echo(user)
