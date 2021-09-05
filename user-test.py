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

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved in the user_list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == "__main__":
    unittest.main()