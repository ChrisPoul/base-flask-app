from . import CLITest
from App.models.user import User


class TestDatabaseCLI(CLITest):

    def test_should_restart_the_database(self):
        users = User.all()
        self.assertEqual(len(users), 1)
        self.cli.invoke(args=["db", "init"])
        users = User.all()
        self.assertEqual(len(users), 0)
