import unittest
from  credentials import Credentials

class TestUser(unittest.TestCase):
    """
    Test that defines test cases for the user class behaviour

    Args:
        unittest.Testcase: Testcase that helps in creating test cases
    """

    def setUp(self):
        """
        set up method that will run before each test case
        """

        self.new_credentials = Credentials("twitter", "cosmic254", "12345")

    def test_init(self):
        """
        will test that the credential object is initialized as expected
        """

        self.assertEqual(self.new_credentials.platfform_name, "twitter")
        self.assertEqual(self.new_credentials.platform_user_name, "cosmic254")
        self.assertEqual(self.new_credentials.platform_user_password, "12345")

    def test_save_credentials(self):
        """
        Test whether the credential object is saved in the credentials list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_requirements), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credentials.credential_requirements = []

    def test_save_multiple_credentials(self):
        """
        test to check whether we can save multiple credentials to out list
        """

        self.new_credentials.save_credentials()
        test_credential = Credentials("instagram" , "Brady", "098765")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_requirements), 2)

    def test_display_all_credentials(self):
        """
        Test whether all credentials are displayed back to the user
        """

        self.assertEqual(Credentials.display_credentials(), Credentials.credential_requirements)




if __name__ == "__main__":
    unittest.main()