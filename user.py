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


