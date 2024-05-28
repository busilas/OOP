class Contacts:
    def __init__(self):
        # Initialize the view to 'quit', an empty contact list, and placeholders for choice and index
        self.view = 'quit'
        self.contact_list = []
        self.choice = None
        self.index = None

    def display(self):
        # Infinite loop to handle different views until 'quit' is selected
        while True:
            if self.view == 'list':
                # Show the list of contacts
                self.show_list()
            elif self.view == 'info':
                # Show detailed information about a contact
                self.show_info()
            elif self.view == 'add':
                # Add a new contact
                print()
                self.add_contact()
            elif self.view == 'quit':
                # Exit the loop and end the display method
                print('\nClosing the contact list...\n')
                break

    def show_list(self):
        # Placeholder method to display the list of contacts
        pass

    def show_info(self):
        # Placeholder method to display information about a specific contact
        pass

    def add_contact(self):
        # Placeholder method to add a new contact
        pass

# Testing the Contacts class
contacts = Contacts()
contacts.display()
