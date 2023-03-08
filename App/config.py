import os

db_dialect = os.environ.get('DB_DIALECT', default='sqlite')
db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='App_db')
db_user = os.environ.get('DB_USERNAME', default='admin')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='3306')
secret_key = os.environ.get('SECRET_KEY', default='dev')
db_uri = f"{db_dialect}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

SECRET_KEY = secret_key
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = db_uri
