class User:
     """
     class that generates a new instance of user 
     """


     user_list = []

     def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

     def save_user(self):
        """
        save_user method saves a user object into user_list
        """
        User.user_list.append(self)

     @classmethod
     def display_users(cls):
        """
        FUnction that returns the user_list
        """

        return cls.user_list

     @classmethod
     def find_by_username(cls, username):
        """
        Method that takes in a number and returns a user that matches the username

        Args:
            username: Username to search for
         Returns:
            User that matches the username
        """
        for user in cls.user_list:
           if user.first_name == username:
              return user


        



