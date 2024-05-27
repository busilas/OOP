# Base class for all vehicles
class Vehicle:
    def __init__(self, make, model, year):
        """
        Initialize a vehicle with make, model, and year.
        
        Parameters:
        make (str): The manufacturer of the vehicle.
        model (str): The model name of the vehicle.
        year (int): The year the vehicle was manufactured.
        """
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False  # Flag to track if the vehicle is running or not

    def start(self):
        """
        Start the vehicle if it's not already running.
        
        This method sets the is_running flag to True and prints a start message.
        """
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} starting...")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    def stop(self):
        """
        Stop the vehicle if it's running.
        
        This method sets the is_running flag to False and prints a stop message.
        """
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} stopping...")
        else:
            print(f"{self.year} {self.make} {self.model} is already stopped.")

# ElectricCar subclass of Vehicle
class ElectricCar(Vehicle):
    def __init__(self, make, model, year, range_per_charge):
        """
        Initialize an electric car with range per charge.
        
        Parameters:
        make (str): The manufacturer of the electric car.
        model (str): The model name of the electric car.
        year (int): The year the electric car was manufactured.
        range_per_charge (int): The maximum range per full charge in miles.
        """
        super().__init__(make, model, year)
        self.range_per_charge = range_per_charge
        self.battery_level = 100  # Assume fully charged initially

    def charge(self):
        """
        Charge the electric car's battery.
        
        This method sets the battery level to 100 and prints a charging message.
        """
        print(f"Charging {self.year} {self.make} {self.model}...")
        self.battery_level = 100  # Fully charge the battery

    def start(self):
        """
        Override start method to check battery level before starting.
        
        If the battery level is above 0, it calls the base class start method.
        Otherwise, it prints a low battery message.
        """
        if self.battery_level > 0:
            super().start()  # Call base class start method
        else:
            print(f"{self.year} {self.make} {self.model} cannot start - low battery.")

# GasolineCar subclass of Vehicle
class GasolineCar(Vehicle):
    def __init__(self, make, model, year, fuel_capacity):
        """
        Initialize a gasoline car with fuel capacity.
        
        Parameters:
        make (str): The manufacturer of the gasoline car.
        model (str): The model name of the gasoline car.
        year (int): The year the gasoline car was manufactured.
        fuel_capacity (int): The maximum fuel capacity in gallons.
        """
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity  # Assume full tank initially

    def refuel(self):
        """
        Refuel the gasoline car's tank.
        
        This method sets the fuel level to the fuel capacity and prints a refueling message.
        """
        print(f"Refueling {self.year} {self.make} {self.model}...")
        self.fuel_level = self.fuel_capacity  # Fill up the fuel tank

# Usage within a driverless car system
if __name__ == "__main__":
    # Create instances of ElectricCar and GasolineCar
    electric_car = ElectricCar("Tesla", "Model S", 2023, 300)
    gasoline_car = GasolineCar("Toyota", "Camry", 2022, 50)

    # Store the vehicles in a list
    vehicles = [electric_car, gasoline_car]

    # Iterate through the vehicles
    for vehicle in vehicles:
        # Start and stop each vehicle
        vehicle.start()
        vehicle.stop()

        # Perform specific actions based on vehicle type
        if isinstance(vehicle, ElectricCar):
            vehicle.charge()  # Charge electric car if it's an ElectricCar instance
        elif isinstance(vehicle, GasolineCar):
            vehicle.refuel()  # Refuel gasoline car if it's a GasolineCar instance
