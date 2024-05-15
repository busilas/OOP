class Person:
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
          self.first_name = first
          self.last_name = last
          self.weight_in_lbs = weight
          self.height_in_inches = height

# Create a new Person object
p = Person('Tom', 'Thumb', 150, 78)


# Print out the attributes of the Person object
print(p.first_name + ' ' + p.last_name + ' weighs ' + str(p.weight_in_lbs) + 'lbs.')
