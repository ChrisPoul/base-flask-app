from . import Test
from App.models.user import User


class CLITest(Test):

    def setUp(self):
        super().setUp()
        self.cli_runner = self.app.test_cli_runner()
        self.user = User(name="Test User")
        self.user.add()


class TestDatabaseCLI(CLITest):

    def test_should_restart_the_database(self):
        users = User.all()
        self.assertEqual(len(users), 1)
        self.cli_runner.invoke(args=["db", "init"])
        users = User.all()
        self.assertEqual(len(users), 0)


class TestUserCLI(CLITest):

    def test_should_create_user(self):
        NEW_NAME = "New User"
        self.cli_runner.invoke(args=["user", "create", "--name", NEW_NAME])
        new_user = User.get_by(name=NEW_NAME)

        self.assertIn(new_user, self.db.session)

    def test_should_delete_user_given_valid_username(self):
        self.cli_runner.invoke(
            args=["user", "delete", "--name", self.user.name]
        )

        self.assertNotIn(self.user, self.db.session)

    def test_should_delete_user_given_valid_username(self):
        self.cli_runner.invoke(
            args=["user", "delete", "--id", self.user.id]
        )

        self.assertNotIn(self.user, self.db.session)
