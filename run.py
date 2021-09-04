from user import User

def create_user(fname, lname, password):
    """
    Function that will create a new user
    """

    new_user = User(fname, lname,password)
    return new_user



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








if __name__ == "__main__":
    main()