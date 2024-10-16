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

Select from the main menu:
1. Register
2. Log in
3. Exit
"""

    print(welcome_banner)
    # Prompt user for input
    user_choice = int(input())

    # Validate user choice
    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    else:
        print("Invalid choice. Please enter a correct choice.")
        main()


# Calling main() function
main()