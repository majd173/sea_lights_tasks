import json
import unittest
from calculator.src.account_class import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        """
        This method sets up the test environment,
        creates a new user and adds it to the list of users.
        """
        self._user = Account()
        self._user.sign_up("pos", "pos")

    def tearDown(self):
        """
        This method cleans up the test environment,
        removes the created user from the list of users.
        """
        self._user.remove_user("pos")

    def test_valid_sign_up(self):
        """
        This method tests valid sign up process.
        """
        self.assertIn("pos", self._user.list_users(), "The user: pos was not added to the list of users")
