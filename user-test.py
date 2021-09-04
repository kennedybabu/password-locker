import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test that defines test cases for the user class behaviour

    Args:
        unittest.Testcase: Testcase that helps in creating test cases
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """

        self.new_user = User("John", "Doe","1234567")

    def test_init(self):
        """
        test_init case to test if the user object is initialized properly
        """

        self.assertEqual(self.new_user.first_name, "John")
        self.assertEqual(self.new_user.last_name, "Doe")
        self.assertEqual(self.new_user.password, "1234567")