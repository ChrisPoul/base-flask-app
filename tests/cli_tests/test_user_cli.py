from click.testing import Result
from . import CLITest
from App.models.user import User


class UserCLITest(CLITest):

    def setUp(self):
        super().setUp()


class TestCreateUser(UserCLITest):

    def test_should_create_user(self):
        NEW_NAME = "New User"
        self.cli.invoke(args=["user", "create", "--name", NEW_NAME])
        new_user = User.get_by(name=NEW_NAME)

        self.assertIn(new_user, self.db.session)


class TestDeleteUser(UserCLITest):

    def test_should_delete_user_given_valid_name(self):
        self.cli.invoke(
            args=["user", "delete", "--name", self.user.name]
        )

        self.assertNotIn(self.user, self.db.session)

    def test_should_delete_user_given_valid_id(self):
        self.cli.invoke(
            args=["user", "delete", "--id", self.user.id]
        )

        self.assertNotIn(self.user, self.db.session)


class TestListUsers(UserCLITest):

    def test_should_return_list_of_all_users(self):
        result: Result = self.cli.invoke(
            args=["user", "list"]
        )

        self.assertIn(self.user.name, result.output)


class TestGetUser(UserCLITest):

    def test_should_return_user_given_valid_id(self):
        result: Result = self.cli.invoke(
            args=["user", "get", "--id", self.user.id]
        )

        self.assertIn(self.user.name, result.output)

    def test_should_return_user_given_valid_name(self):
        result: Result = self.cli.invoke(
            args=["user", "get", "--name", self.user.name]
        )

        self.assertIn(self.user.id, result.output)

    def test_should_not_retu(self):
        result: Result = self.cli.invoke(
            args=["user", "get", "--name", self.user.name]
        )

        self.assertIn(self.user.id, result.output)
