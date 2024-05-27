from passenger_interaction import User, PassengerInteraction

class DriverlessCarSystem:
    """
    Represents the main driverless car system.
    """

    def __init__(self):
        """
        Initializes a DriverlessCarSystem instance.
        """
        self.users = []
        self.passenger_interaction = PassengerInteraction()
        self.current_user = None  # Track the currently logged-in user

    def login(self):
        """
        Log in a user by verifying credentials.
        """
        account_name = input("Enter account name: ")
        for user in self.users:
            if user.account_name == account_name:
                password = input("Enter password: ")
                if user.verify_password(password):
                    self.current_user = user  # Set the current user after successful login
                    print(f"Login successful! Welcome {user.first_name} {user.last_name}.")
                    return
                else:
                    print("Incorrect password. Please try again.")
                    return
        print("User not found. Please sign up first.")

    def logout(self):
        """
        Log out the current user.
        """
        if self.current_user:
            print(f"Logging out user: {self.current_user.account_name}")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def signup(self):
        """
        Register a new user.
        """
        user = User()
        self.users.append(user)
        print("User signed up successfully!")

    def user_menu(self):
        """
        Display and handle the user menu options for logged in users.
        """
        while self.current_user:
            print("\n=== User Menu ===")
            print("1. Set Destination")
            print("2. Search Destination")
            print("3. Edit Destination")
            print("4. Delete Destination")
            print("5. Start Journey")
            print("6. Stop Journey")
            print("7. Log Out")
            print("0. Exit")

            choice = input("Enter your choice (0-7): ")

            if choice == "1":
                location = input("Enter location: ")
                destination = input("Enter destination: ")
                self.passenger_interaction.set_destination(location, destination)

            elif choice == "2":
                location = input("Enter location to search: ")
                result = self.passenger_interaction.search_destination(location)
                if result:
                    print(f"Destination at location '{location}': {result}")
                else:
                    print(f"No destination found for location '{location}'.")

            elif choice == "3":
                location = input("Enter location to edit: ")
                new_destination = input("Enter new destination: ")
                self.passenger_interaction.edit_destination(location, new_destination)

            elif choice == "4":
                location = input("Enter location to delete destination: ")
                self.passenger_interaction.delete_destination(location)

            elif choice == "5":
                self.passenger_interaction.start_journey()

            elif choice == "6":
                self.passenger_interaction.stop_journey()

            elif choice == "7":
                self.logout()

            elif choice == "0":
                print("Exiting...")
                exit()

            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        """
        Display and handle the main menu options.
        """
        while True:
            print("\n=== Driverless Car System ===")
            print("1. Log In")
            print("2. Sign Up")
            print("3. Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.login()
                if self.current_user:
                    self.user_menu()

            elif choice == "2":
                self.signup()

            elif choice == "3":
                print("Quitting...")
                break

            else:
                print("Invalid choice. Please try again.")
