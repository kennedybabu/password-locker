from user import User

def create_user(fname, lname, password):
    """
    Function that will create a new user
    """

    new_user = User(fname, lname,password)
    return new_user