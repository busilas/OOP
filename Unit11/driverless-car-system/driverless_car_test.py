import unittest
from driverless_car import DriverlessCar

class TestDriverlessCar(unittest.TestCase):
    """
    Unit test class for the DriverlessCar class.
    """

    def setUp(self):
        """
        Set up the test case with an instance of DriverlessCar.
        """
        self.car = DriverlessCar('ModelX', 50.0)

    def test_initialization(self):
        """
        Test the initialization of the DriverlessCar instance.
        """
        # Verify initial values of car model, speed, and steering angle
        self.assertEqual(self.car.carModel, 'ModelX')
        self.assertEqual(self.car.carSpeed, 50.0)
        self.assertEqual(self.car.steeringAngle, 0.0)

    def test_set_get_car_model(self):
        """
        Test setting and getting the car model.
        """
        # Set car model to 'ModelS'
        self.car.set_car_model('ModelS')
        # Verify the car model is updated correctly
        self.assertEqual(self.car.get_car_model(), 'ModelS')

    def test_set_get_car_speed(self):
        """
        Test setting and getting the car speed.
        """
        # Set car speed to 60.0
        self.car.set_car_speed(60.0)
        # Verify the car speed is updated correctly
        self.assertEqual(self.car.get_car_speed(), 60.0)

    def test_set_get_steering_angle(self):
        """
        Test setting and getting the steering angle.
        """
        # Set steering angle to 15.0 degrees
        self.car.set_steering_angle(15.0)
        # Verify the steering angle is updated correctly
        self.assertEqual(self.car.get_steering_angle(), 15.0)

    def test_apply_brake(self):
        """
        Test applying the brake to stop the car.
        """
        # Apply the brake to stop the car
        self.car.apply_brake()
        # Verify the car speed is set to 0.0
        self.assertEqual(self.car.get_car_speed(), 0.0)

if __name__ == '__main__':
    unittest.main()
