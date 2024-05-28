class Contacts:
    def __init__(self):
        # Initialize the view to 'list' to show the list view first
        self.view = 'list'
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
        # Print a blank line for legibility
        print()
        if len(self.contact_list) == 0:
            # If contact list is empty, present the user with options to add a contact or quit
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            # If contact list is not empty, list all contacts with index numbers
            for index, contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            # Present the user with options to select a contact, add a new contact, or quit
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
        # Handle the user's choice
        self.handle_choice()

    def handle_choice(self):
        # Handle user choice: 'q' to quit, 'a' to add a contact, or a number to select a contact
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'
        elif self.choice.isnumeric() and self.view == 'list':
            index = int(self.choice) - 1
            if 0 <= index < len(self.contact_list):
                self.index = index
                self.view = 'info'

    def show_info(self):
        # Display detailed information about the selected contact
        contact = self.contact_list[self.index]
        print(f"\nFirst Name: {contact.first_name}")
        print(f"Last Name: {contact.last_name}")
        print(f"Personal Phone: {contact.personal_phone}")
        print(f"Personal Email: {contact.personal_email}")
        print(f"Work Phone: {contact.work_phone}")
        print(f"Work Email: {contact.work_email}")
        print(f"Title: {contact.title}\n")
        # After showing the information, revert back to the list view
        self.view = 'list'

    def __add__(self, new_contact):
        # Overload the + operator to add a new contact to the contact list
        self.contact_list.append(new_contact)

    def add_contact(self):
        # Add a new contact by creating an Information object and adding it to the contact list
        self + Information()
        # Revert back to the list view after adding a contact
        self.view = 'list'

# The Information class used to store contact details
class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')

# Testing the code
contacts = Contacts()
contacts.display()
