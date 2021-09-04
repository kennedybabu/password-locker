from user import User

def create_user(fname, lname, password):
    """
    Function that will create a new user
    """

    new_user = User(fname, lname,password)
    return new_user



def main():
    print("Jambo(Hello, in Swahili)!Welcome to Shhh-Locker!")








if __name__ == "__main__":
    main()