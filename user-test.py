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

    def tearDown(self):
        """
        tearDown method will clean up after each test case has run
        """

        User.user_list = []

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

    def test_display_all_users(self):
        """
        Test to ensure all users are returned
        """

        self.assertEqual(User.display_users(), User.user_list)

    def test_find_user_by_username(self):
        """
        Test to see if we can find a user by their username
        """

        self.new_user.save_user()
        test_user = User("John", "Doe", "1234567")
        test_user.save_user()

        found_user = User.find_by_username("John")
        self.assertEqual(found_user.first_name, test_user.first_name)




if __name__ == "__main__":
    unittest.main()