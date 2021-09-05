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
        Credentials.credential_requirements.append(self)

    def delete_credentials(self):
        """
        Function that will delete a users crededntials
        """
        Credentials.credential_requirements.remove(self)


    @classmethod
    def display_credentials(cls):
        """
        display_credentials returns the credentials list
        """
        return cls.credential_requirements

    @classmethod
    def find_credentials(cls, platform):
        """
        Function that will take in a platform name and returns the credentials that match

        Args:
            platform_name: name of the credential to search for
        Returns:
            Credentials that match the platform_name
        """
        for credential in cls.credential_requirements:
            if credential.platfform_name == platform:
                return credential