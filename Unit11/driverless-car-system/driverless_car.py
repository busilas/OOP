class DriverlessCar:
    """
    Represents a driverless car with model, speed, steering angle, and brake attributes.
    """

    def __init__(self, carModel, carSpeed, steeringAngle=0.0):
        """
        Initializes a DriverlessCar instance.

        Args:
            carModel (str): The model of the car.
            carSpeed (float): The speed of the car.
            steeringAngle (float, optional): The initial steering angle of the car. Defaults to 0.0.
        """
        self.carModel = carModel
        self.carSpeed = carSpeed
        self.steeringAngle = steeringAngle

    def set_car_model(self, model):
        """
        Set the model of the car.

        Args:
            model (str): The new model of the car.
        """
        self.carModel = model

    def get_car_model(self):
        """
        Get the model of the car.

        Returns:
            str: The model of the car.
        """
        return self.carModel

    def set_car_speed(self, speed):
        """
        Set the speed of the car.

        Args:
            speed (float): The new speed of the car.
        """
        self.carSpeed = speed

    def get_car_speed(self):
        """
        Get the speed of the car.

        Returns:
            float: The speed of the car.
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
