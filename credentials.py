class Credentials:
    """
    class that generates an instance of credential 
    """

    credential_requirements = []


    def __init__(self, platform_name, platform_user_name, platform_user_password):

        self.platfform_name = platform_name
        self.platform_user_name = platform_user_name
        self.platform_user_password = platform_user_password

    def save_credentials(self):
        """
        Method that saves a credential object in the credential_requirements array
        """


    @classmethod
    def display_credentials(cls):
        """
        display_credentials returns the credentials list
        """

        return cls.credential_requirements