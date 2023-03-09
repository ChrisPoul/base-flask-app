from .. import Test
from App.models.user import User


class CLITest(Test):

    def setUp(self):
        super().setUp()
        self.cli = self.app.test_cli_runner()
        self.user = User(name="Test User")
        self.user.add()
