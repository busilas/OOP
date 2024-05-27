#######################################################################
#Encapsulation Exercise 3
#######################################################################

class BankAccount:
    def __init__(self):
        self._checking = 0.0
        self._savings = 0.0

    def set_checking(self, amount):
        self._checking = amount

    def set_savings(self, amount):
        self._savings = amount

    def get_checking(self):
        return self._checking

    def get_savings(self):
        return self._savings

# Initialize an object of the BankAccount class
my_account = BankAccount()

# Set values using setters
my_account.set_checking(523.48)
my_account.set_savings(386.15)

# Get values using getters
print(my_account.get_checking())
print(my_account.get_savings())