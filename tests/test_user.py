from . import Test


class UserTest(Test):

    def setUp(self):
        super().setUp()


class TestDoSomething(UserTest):

    def test_should_pass(self):
        self.assertTrue(True)
