class Person:
    def __init__(self, name, age, occupation):
        self._name = name
        self._age = age
        self._occupation = occupation

    # Getter and setter methods for name attribute
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # Getter and setter methods for age attribute
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    # Getter and setter methods for occupation attribute
    def get_occupation(self):
        return self._occupation

    def set_occupation(self, new_occupation):
        self._occupation = new_occupation

# Test the class with the expected output
my_person = Person("Citra Curie", 16, "student")

# Displaying the initial values
print("The method get_name() returns", my_person.get_name())
print("The method get_age() returns", my_person.get_age())
print("The method get_occupation() returns", my_person.get_occupation())

# Changing attributes using setters
my_person.set_name("Rowan Faraday")
my_person.set_age(18)
my_person.set_occupation("plumber")

# Displaying the changed values
print("After changes:")
print("The method get_name() returns", my_person.get_name())
print("The method get_age() returns", my_person.get_age())
print("The method get_occupation() returns", my_person.get_occupation())