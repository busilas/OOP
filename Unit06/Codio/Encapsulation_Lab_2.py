import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._new_coffee = []
        self._old_coffee = self.load_coffee()

    def load_coffee(self):
        coffee = []
        try:
            with open(self._file) as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    coffee.append(row)
        except FileNotFoundError:
            # If file not found, initialize with headers
            coffee.append(["Roaster", "Country", "Region", "Stars"])
        return coffee

    @property
    def roaster(self):
        return self._roaster

    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, new_region):
        self._region = new_region

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

    def add_coffee(self, roaster, country, region, stars):
        self._roaster = roaster
        self._country = country
        self._region = region
        self._stars = stars
        self._new_coffee.append([self._roaster, self._country, self._region, self._stars])

    def save_coffee(self):
        with open(self._file, mode='w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            # Write old coffee entries
            for row in self._old_coffee:
                writer.writerow(row)
            # Write new coffee entries
            for row in self._new_coffee:
                writer.writerow(row)

    def display_coffee(self):
        for row in self._old_coffee:
            print(", ".join(row))
        for row in self._new_coffee:
            print(", ".join(row))


# **********************************************
# code for testing your script
# **********************************************

test_object = CoffeeJournal("test_journal2.csv")
test_object.roaster = "Peace River"
test_object.country = "Rwanda"
test_object.region = "Remera"
test_object.stars = "***"
print(test_object.roaster)
print(test_object.country)
print(test_object.region)
print(test_object.stars)
