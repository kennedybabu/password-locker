from user import User
from credentials import Credentials

def create_user(fname, lname, password):
    """
    Function that will create a new user
    """

    new_user = User(fname, lname,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """

    user.save_user()

def display_credentials():
    """
    A function that will return the credential list
    """
    return User.display_credentials()





def main():
    print("Jambo(Hello, in Swahili)!Welcome to Shhh-Locker!.")
    print("\n")

    user_name = input("Enter your user name: ")

    print(f"What would you like to do? A. Login | B. Create an account")

    short_code = input().lower()

    while True:
        if short_code == "a":
            print("Already a User")
            print("_"*3)

            print("Enter your user name: ")
            user_Name = input()

            print("Enter your password: ")
            user_password = input()

            print("We are trying")

            break



        elif short_code == "b":

            print("Create an Account")

            new_user_first_name = input("Enter your first name: ")
            new_user_last_name = input("Enter your last name: ")
            print("Would you like to create your password or generate one, A. Create | B. Generate")
            create_password = input().lower()

            new_user_password = input("Enter your password: ")

            save_user(create_user(new_user_first_name, new_user_last_name, new_user_password))
            print("\n")
            print(f"New User {new_user_first_name} {new_user_last_name} created!")

            print("Create password: ")

            platfrm_usrname  = input("Enter your user name")
            platform = input("Enter platform name...")
            platform_pswrd = input("Enter password..")

            print(f"Account for {platform} with the username {platfrm_usrname} created")


            print("Bye")
            break










if __name__ == "__main__":
    main()