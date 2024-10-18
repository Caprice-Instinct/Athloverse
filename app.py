def add_item():
    """
    Adding a new sports item to the list
    User is directed to sports_menu whether the item is
    added successfully or not.
    """

    # Add item banner
    add_banner = """
+++++==============================+++++
+              ADD ITEM                +
+--------------------------------------+
+   SPORTS GEAR, CLOTHES, EQUIPMENT    +
+++++==============================+++++

Kindly input the details for the item below:
    """

    print(add_banner)

    # Prompt user for number of items to be added
    items = int(input("How many items do you want to add? "))

    if items < 0:
        # Display error message
        print("No negative values.")

        # Redirect back to add sport item
    else:
        pass

    for item in range(items):
        # Prompt user for item details
        item_id = int(input("Enter the item ID: "))
        item_name = input("Enter the item name: ")
        item_category = input("Enter the item category: ")
        item_purchase_date = input("Enter the item purchase date: ")
        item_price = float(input("Enter the unit price of the item: "))
        item_quantity = int(input("Enter the quantity of item: "))

        # TODO : Save data

        # Success message
        print(f"{item_name} added successfully.")

    # Redirect to menu page
    sports_menu()


def update_item():
    """
    Making changes to item details of existing items.
    Manager redirected to menu page upon update.
    """

    # Update banner
    update_banner = """
+++++==============================+++++
+            UPDATE ITEM               +
+--------------------------------------+
+   SPORTS GEAR, CLOTHES, EQUIPMENT    +
+++++==============================+++++
"""

    print(update_banner)

    # Display items
    display_items()
    # Prompt user to choose item to update
    item_to_update = int(input("Which item would you like to update? "))


def delete_item(item):
    """
    Deleting an existing item from stock.
    Manager is directed to menu page after deletion.
    :param item: Item in stock to be deleted
    """

    # Delete banner
    delete_banner = """
+++++==============================+++++
+           DELETE ITEM                +
+--------------------------------------+
+   SPORTS GEAR, CLOTHES, EQUIPMENT    +
+++++==============================+++++
    """

    print(delete_banner)

    # Display all existing items
    display_items()
    # Prompt user to choose item to delete
    item_to_delete = int(input("Which item would you like to delete? "))


def display_items():
    """
    Display existing items in stock
    :return: Items in stock
    """

    # Display banner
    display_banner = """
+++++==============================+++++
+           DISPLAY ITEMS              +
+--------------------------------------+
+   SPORTS GEAR, CLOTHES, EQUIPMENT    +
+++++==============================+++++

The following are the items in stock:

    """

    print(display_banner)


def logout():
    """
    Logs out the user
    """
    user_choice = input("Are you sure you want to exit? (Y/N): ")

    if user_choice == "Y" or user_choice == "y":
        # Success message upon logout
        print("Log out successful. Redirecting to login page...")

        # Redirect to login page
        login_page()

    else:
        # Display redirect message
        print("Redirecting to the sports menu page...")

        # Redirect user to the main menu
        sports_menu()


def exit_sports_menu():
    """
    Allows user to exit the sports menu to main menu
    """
    user_choice = input("Are you sure you want to exit? (Y/N): ")

    if user_choice == "Y" or user_choice == "y":
        # Success message upon logout
        print("Log out successful. Redirecting to login page...")

        # Redirect to login page
        login_page()

    else:
        # Display redirect message
        print("Redirecting to the main menu page...")

        # Redirect user to the main menu
        main_menu()


def sports_menu():
    """
    Sports menu is displayed here for adding, updating, deleting and
    viewing sports equipment.
    """

    # Sports banner
    sports_banner = """
+++++==============================+++++
+            SPORTS MENU               +
+--------------------------------------+
+   SPORTS GEAR, CLOTHES, EQUIPMENT    +
+++++==============================+++++

What would you like to do:
1. Add a new item.
2. Update an existing item.
3. Delete an item.
4. Display items.
5. Logout.
6. Exit the sports menu.
"""
    print(sports_banner)

    # Prompt user for a choice
    user_choice = int(input())

    # Validate user choice
    if user_choice == 1:
        print("Adding a new item...")
        add_item()
    elif user_choice == 2:
        print("Updating an item.")
        update_item()
    elif user_choice == 3:
        print("Deleting an item.")
        delete_item()
    elif user_choice == 4:
        print("Displaying items in stock.")
        display_items()
    elif user_choice == 5:
        logout()
    elif user_choice == 6:
        exit_sports_menu()
    else:
        # Display error message
        print("Invalid choice. Please enter a correct choice.")

        # Redirect the user back to sports_menu
        sports_menu()


def exit_program():
    """
    Smoothly terminates user program.
    """
    user_choice = input("Are you sure you want to exit? (Y/N): ")

    if user_choice == "Y" or user_choice == "y":
        print("Exiting the program...")
        exit()

    else:
        # Display redirect message
        print("Redirecting to the main menu...")

        # Redirect user to the main menu
        main_menu()


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
+++++==============================+++++

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
+++++==============================+++++

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
    print(f"Registration successful. Welcome {manager_name} to Athloverse.")

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
        exit_program()

    else:
        # Display error message
        print("Invalid choice. Please enter a correct choice.")

        # Redirect user to retry entering right choice
        main_menu()


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

    # Go to main menu
    main_menu()


# Calling main() function
main()