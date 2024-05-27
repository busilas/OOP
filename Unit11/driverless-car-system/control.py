from passenger_interaction import DriverlessCar
from environmental_perception import EnvironmentalPerception
from navigation import Navigation

class Control:
    """
    Controls a driverless car by adjusting speed and steering angle based on environmental perception and navigation.

    Attributes:
        vehicle (DriverlessCar): The driverless car instance to control.
        environmentalPerception (EnvironmentalPerception): Environmental perception module for obstacle detection.
        navigation (Navigation): Navigation module for route planning.
        current_speed (float): The current speed set for the vehicle in meters per second.
        steering_angle (float): The current steering angle set for the vehicle in degrees.
    """

    def __init__(self, vehicle):
        """
        Initializes a Control instance for a driverless car.

        Args:
            vehicle (DriverlessCar): The driverless car instance to control.
        """
        self.vehicle = vehicle
        self.environmentalPerception = EnvironmentalPerception()
        self.navigation = Navigation()
        self.current_speed = 0.0
        self.steering_angle = 0.0

    def accelerate(self, acceleration):
        """
        Accelerate the vehicle by adjusting the current speed.

        Args:
            acceleration (float): The acceleration value in meters per second squared.

        Raises:
            ValueError: If acceleration is a negative value.
        """
        if acceleration >= 0:
            self.current_speed += acceleration
        else:
            raise ValueError("Acceleration must be a positive value.")

    def brake(self, deceleration):
        """
        Apply brakes to slow down the vehicle by adjusting the current speed.

        Args:
            deceleration (float): The deceleration value in meters per second squared.

        Raises:
            ValueError: If deceleration is a negative value.
        """
        if deceleration >= 0:
            self.current_speed -= deceleration
            if self.current_speed < 0:
                self.current_speed = 0.0
        else:
            raise ValueError("Deceleration must be a positive value.")

    def steer(self, steering_angle):
        """
        Adjust the steering angle of the vehicle.

        Args:
            steering_angle (float): The new steering angle in degrees.

        Raises:
            ValueError: If the steering angle is outside the valid range [-30, 30] degrees.
        """
        if -30 <= steering_angle <= 30:
            self.steering_angle = steering_angle
        else:
            raise ValueError("Steering angle must be between -30 and 30 degrees.")

    def updateVehicleDynamics(self):
        """
        Update the vehicle's speed and steering angle based on the current settings.
        """
        self.vehicle.set_car_speed(self.current_speed)
        self.vehicle.set_steering_angle(self.steering_angle)

    def updateSensorData(self):
        """
        Update sensor data by processing environmental perception.
        """
        self.environmentalPerception.processSensorData()

    def detectAndAvoidObstacles(self):
        """
        Detect and avoid obstacles based on environmental perception data.
        """
        self.environmentalPerception.detectObstacles()
        risk_level = self.environmentalPerception.assessObstacleRisk()

        if risk_level == "High risk detected. Avoidance maneuver required.":
            self.brake(5.0)  # Simulate braking to avoid collision
            self.steer(10.0)  # Simulate steering to avoid obstacles

    def navigate(self, start, destination):
        """
        Navigate from start to destination using the navigation module.

        Args:
            start (tuple): The starting coordinates (latitude, longitude).
            destination (tuple): The destination coordinates (latitude, longitude).
        """
        self.navigation.plan_route(start, destination)

    def follow_route(self):
        """
        Follow the planned route and adjust vehicle dynamics accordingly.
        """
        while not self.navigation.has_reached_destination():
            next_waypoint = self.navigation.get_next_waypoint()
            if next_waypoint:
                current_position = self.environmentalPerception.gps.getCoordinates()
                distance = self.navigation.calculate_distance(current_position, next_waypoint)
                if distance < 0.001:
                    continue  # Already at the waypoint

                # Simplified steering logic
                if next_waypoint[0] > current_position[0]:
                    self.steer(5.0)
                elif next_waypoint[0] < current_position[0]:
                    self.steer(-5.0)

                self.accelerate(2.0)
                self.updateVehicleDynamics()
                self.updateSensorData()
                self.detectAndAvoidObstacles()
                self.updateVehicleDynamics()
