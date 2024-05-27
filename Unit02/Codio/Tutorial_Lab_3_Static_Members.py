class Person:
    count = 0  # Static variable to track the number of Person instances
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count += 1  # Increment the static variable each time a new instance is created

    def calc_bmi(self):
        """Calculate and return the BMI for the person."""
        return (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)


# Create two Person objects
p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

# Calculate and print the BMIs
print(p.calc_bmi())
print(p2.calc_bmi())

# Print the number of Person instances created
print(Person.count)
