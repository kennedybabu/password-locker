from user import User
from credentials import Credentials
import random

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

def create_user_credentials(platform_name, platform_username, platform_password):
    """
    Function that will create a new credential
    """
    new_user_credentials = Credentials(platform_name, platform_username, platform_password)

def save_user_credentials(credential):
    """
    Function to save user credentials
    """
    Credentials.save_credentials(credential)

def display_credentials():
    """
    A function that will return the credential list
    """
    return User.display_credentials()



def main():
    print("\n")
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

            if create_password == "a":
                create_password = input("Enter your password: ")
                confirmed_password = input("Confirm password: ")
                if confirmed_password == create_password:
                    print("Account Created Succesfully.")
                else:
                    print("Password Doesn't match. Try again")
                    break
            elif create_password == "b":
                chars = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"]

                while 1:
                    password_length = int(input("What length would you like your password to be,i.e 5,8..."))
                     
                    for i in range(0,2):
                        password_generated = ""
                        for i in range(0, password_length):
                            password_char = random.choice(chars)
                            password_generated = password_generated + password_char
                            print(password_generated)


            new_user_password = input("Enter your password: ")

            save_user(create_user(new_user_first_name, new_user_last_name, new_user_password))
            print("\n")
            print(f"New User {new_user_first_name} {new_user_last_name} created!")


            print("Proceed to login")

            login_name = input("Enter your name: ")
            login_password = input("Enter password: ")

            if login_name == new_user_first_name and login_password == new_user_password:
                print("Login successful!")

                print("Create a Password Vault")
                platform = input("Enter platform name...")
                platform_username  = input("Enter your user name")
                platform_pswrd = input("Enter password..")

                save_user_credentials(create_user_credentials(platform,platform_username,  platform_pswrd))

                # save_credentials()

                print(f"Password Vault for {platform} with the username {platform_username} created successfully")


            else:
                print("Login Failed. Enter valid credentials")
                break        



            print("Bye")
            break










if __name__ == "__main__":
    main()