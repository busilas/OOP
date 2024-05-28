class Chef:
    def __init__(self, name, cuisine, stars):
        # Initialize Chef object with name, cuisine, and Michelin stars
        self.name = name
        self.cuisine = cuisine
        self.michelin_stars = stars
    
    def __lt__(self, other):
        # Overload the < (less than) operator to compare Michelin stars
        return self.michelin_stars < other.michelin_stars
    
    def compare(self, other_chef):
        # Compare Michelin stars between two chefs and return a string indicating the result
        if self < other_chef:
            # If self has fewer stars than other_chef, return a string indicating that other_chef has more stars
            return f'{other_chef.name} has more Michelin stars than {self.name}'
        else:
            # If self has equal or more stars than other_chef, return a string indicating that self has more stars
            return f'{self.name} has more Michelin stars than {other_chef.name}'

# Instantiate Chef objects
marco = Chef('Marco Pierre White', 'French, British', 3)
rene = Chef('Rene Redzepi', 'Nordic', 2)

# Testing the compare method
print(marco.compare(rene))  # Output: ‘Marco Pierre White has more Michelin stars than Rene Redzepi’
print(rene.compare(marco))  # Output: ‘Marco Pierre White has more Michelin stars than Rene Redzepi’
