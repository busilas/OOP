class Person:
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

    def calc_bmi(self):
        """Calculate and return the BMI for the person."""
        return (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)


# Create two Person objects
p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

# Calculate and print the BMIs
print(p.calc_bmi())
print(p2.calc_bmi())
