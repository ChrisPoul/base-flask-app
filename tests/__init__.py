import unittest
from flask_testing import TestCase
from flask.testing import FlaskClient
from App import create_app
from App.models import database


class Test(TestCase, unittest.TestCase):

    def create_app(self):
        test_config = {
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "TESTING": True
        }
        app = create_app(test_config)

        return app

    def setUp(self):
        self.client: FlaskClient = self.app.test_client()
        self.db = database
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
