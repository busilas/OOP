#######################################################################
#Encapsulation Exercise 1
#######################################################################

class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

# Initialize an object of the Country class
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Display the attributes of the country
print(my_country._name)
print(my_country._capital)
print(my_country._population)
print(my_country._continent)