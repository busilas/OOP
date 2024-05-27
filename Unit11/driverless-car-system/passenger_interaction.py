class User:
    """
    Represents a user in the driverless car system, with functionalities
    to manage user details, login, and registration.
    """
    next_id = 1  # Static variable for user ID

    def __init__(self):
        """
        Initializes a User instance, prompting the user to enter their details.
        """
        self.user_ID = User.next_id
        User.next_id += 1
        self.first_name = input('Enter your first name: ')
        self.last_name = input('Enter your last name: ')
        self.account_name = input('Enter an account name: ')
        self.password = input('Enter a password: ')
        self.email = input('Enter your email address: ')

    def __repr__(self):
        """
        Represent the User instance as a string.
        """
        return f'User ({self.user_ID}) {self.account_name}'

    def verify_password(self, password):
        """
        Verify if the provided password matches the user's password.

        Args:
            password (str): The password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return self.password == password


class PassengerInteraction:
    """
    Manages interactions related to passenger destinations and journey.
    """

    def __init__(self):
        """
        Initializes a PassengerInteraction instance.
        """
        self.destinations = {}
        self.journey_started = False

    def set_destination(self, location, destination):
        """
        Set a destination for a specific location.

        Args:
            location (str): The location to set the destination for.
            destination (str): The destination to set.
        """
        self.destinations[location] = destination
        print(f"Destination '{destination}' set for location '{location}'.")

    def search_destination(self, location):
        """
        Search for a destination at a specified location.

        Args:
            location (str): The location to search for a destination.

        Returns:
            str: The destination at the specified location, or None if not found.
        """
        return self.destinations.get(location)

    def edit_destination(self, location, new_destination):
        """
        Edit the destination at a specified location.

        Args:
            location (str): The location to edit the destination for.
            new_destination (str): The new destination to set.
        """
        if location in self.destinations:
            self.destinations[location] = new_destination
            print(f"Destination for location '{location}' updated to '{new_destination}'.")
        else:
            print(f"No destination found for location '{location}'.")

    def delete_destination(self, location):
        """
        Delete the destination at a specified location.

        Args:
            location (str): The location to delete the destination for.
        """
        if location in self.destinations:
            del self.destinations[location]
            print(f"Destination for location '{location}' deleted.")
        else:
            print(f"No destination found for location '{location}'.")

    def start_journey(self):
        """
        Start the journey for the passenger.
        """
        if not self.journey_started:
            self.journey_started = True
            print("Journey started.")
        else:
            print("Journey is already in progress.")

    def stop_journey(self):
        """
        Stop the journey for the passenger.
        """
        if self.journey_started:
            self.journey_started = False
            print("Journey stopped.")
        else:
            print("No journey is currently in progress.")


class DriverlessCar:
    """
    Represents a driverless car with basic functionalities for speed and steering.
    """

    def __init__(self, carModel, carSpeed):
        """
        Initializes a DriverlessCar instance.

        Args:
            carModel (str): The model of the car.
            carSpeed (float): The initial speed of the car in meters per second.
        """
        self.carModel = carModel
        self.carSpeed = carSpeed
        self.steeringAngle = 0.0

    def set_car_speed(self, speed):
        """
        Set the speed of the car.

        Args:
            speed (float): The new speed of the car in meters per second.
        """
        self.carSpeed = speed

    def get_car_speed(self):
        """
        Get the current speed of the car.

        Returns:
            float: The current speed of the car.
        """
        return self.carSpeed

    def set_steering_angle(self, angle):
        """
        Set the steering angle of the car.

        Args:
            angle (float): The new steering angle of the car.
        """
        self.steeringAngle = angle

    def get_steering_angle(self):
        """
        Get the steering angle of the car.

        Returns:
            float: The steering angle of the car.
        """
        return self.steeringAngle

    def apply_brake(self):
        """
        Apply the brakes of the car, reducing its speed to zero.
        """
        self.carSpeed = 0
