import json
import unittest
from calculator.src.account_class import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        """
        This method sets up the test environment,
        creates a new user and adds it to the list of users.
        """
        Account.sign_up("pos", "123456")

    def tearDown(self):
        """
        This method cleans up the test environment,
        removes the created user from the list of users.
        """
        Account.remove_user("pos")

    def test_valid_sign_up(self):
        """
        This method tests valid sign up process.
        """
        self.assertIn("pos", Account.list_users(), "The user: pos was not added to the list of users")
