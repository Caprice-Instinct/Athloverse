def login_page():
    """
    User login page for their credentials: email address and password.
    Redirects user to sports menu page.
    """

    # Login banner
    login_banner = """
+++++==============================+++++
+             LOGIN PAGE               +
+--------------------------------------+
+ALready have an account? Sign in here.+
+++++=========================++++++++++

Fill in your email address and password below:
"""

    print(login_banner)

    # Prompt user for email address and password

    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Verify email address and password
    if email_address == "linet@gmail.com" and password == '12345':
        # Redirect user to menu page
        print("Log in successful.")
        sports_menu()
    else:
        print("You entered the wrong details. Please try again.")

        # Redirect user to main page upon unsuccessful login
        main()



def registration_page():
    """
    User registration page for their details.
    Redirect users to main page after registration.
    """
    # Registration banner
    registration_banner = """
+++++==============================+++++
+          REGISTRATION PAGE           +
+--------------------------------------+
+Don't have an account? Create one here+
+++++=========================++++++++++

Fill in the necessary details below:
"""
    print(registration_banner)

    # Prompting the manager for details
    manager_id = int(input("Enter your manager ID: "))
    manager_name = input("Enter your full name: ")
    years_of_experience = int(input("Enter your years of experience: "))
    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")
    phone_number = int(input("Enter your phone number: "))

    # Welcoming new user
    print(f"TRegistration successful. Welcome {manager_name} to Athloverse.")

    # Redirect to main page
    print("Redirecting to main page...")
    main()


def main_menu():
    """
    Displays the main menu with user options such as register,
    login and exiting the program.
    """

    # Menu containing user options
    menu = """
Select from the main menu:
1. Register
2. Log in
3. Exit
    """
    print(menu)
    # Prompt user for input
    user_choice = int(input())

    # Validate user choice
    if user_choice == 1:
        registration_page()
    elif user_choice == 2:
        login_page()
    elif user_choice == 3:
        pass
    else:
        print("Invalid choice. Please enter a correct choice.")
        main()


def main():
    """
    Displays main welcome page
    """

    # Welcome banner
    welcome_banner = """
+++++==============================+++++
+         WELCOME TO ATHLOVERSE        +
+--------------------------------------+
+    CLOTHES, EQUIPMENT, NAME IT...    +
+++++==============================+++++
"""

    print(welcome_banner)
    main_menu()


# Calling main() function
main()
