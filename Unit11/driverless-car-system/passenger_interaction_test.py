import unittest
from unittest.mock import patch
from passenger_interaction import User, PassengerInteraction, DriverlessCar

class TestUser(unittest.TestCase):
    """
    Unit test case for testing the User class.
    """

    @patch('builtins.input', side_effect=['John', 'Doe', 'johndoe', 'password123', 'john@example.com'])
    def setUp(self, mock_inputs):
        """
        Set up the test case environment. Initialize the User instance with mock inputs.
        
        Args:
            mock_inputs (MagicMock): Mocked input for the User initialization.
        """
        self.user = User()

    def test_user_initialization(self):
        """
        Test the initialization of the User instance.
        """
        # Verify if the user attributes are set correctly
        self.assertEqual(self.user.user_ID, 1)
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.account_name, 'johndoe')
        self.assertEqual(self.user.password, 'password123')
        self.assertEqual(self.user.email, 'john@example.com')

    def test_verify_password(self):
        """
        Test the verify_password method of the User class.
        """
        # Verify correct password
        self.assertTrue(self.user.verify_password('password123'))
        # Verify incorrect password
        self.assertFalse(self.user.verify_password('wrongpassword'))

class TestPassengerInteraction(unittest.TestCase):
    """
    Unit test case for testing the PassengerInteraction class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the PassengerInteraction instance.
        """
        self.pi = PassengerInteraction()

    def test_set_and_search_destination(self):
        """
        Test setting and searching for a destination.
        """
        # Set a destination
        self.pi.set_destination('Home', '123 Main St')
        # Verify if the destination is set correctly
        self.assertEqual(self.pi.search_destination('Home'), '123 Main St')
        # Verify if a non-existent destination returns None
        self.assertIsNone(self.pi.search_destination('Work'))

    def test_edit_destination(self):
        """
        Test editing an existing destination.
        """
        # Set and then edit a destination
        self.pi.set_destination('Home', '123 Main St')
        self.pi.edit_destination('Home', '456 Elm St')
        # Verify if the destination is edited correctly
        self.assertEqual(self.pi.search_destination('Home'), '456 Elm St')
        # Try to edit a non-existent destination
        self.pi.edit_destination('Work', '789 Oak St')  # Should not find location

    def test_delete_destination(self):
        """
        Test deleting a destination.
        """
        # Set and then delete a destination
        self.pi.set_destination('Home', '123 Main St')
        self.pi.delete_destination('Home')
        # Verify if the destination is deleted
        self.assertIsNone(self.pi.search_destination('Home'))
        # Try to delete a non-existent destination
        self.pi.delete_destination('Work')  # Should not find location

    def test_start_and_stop_journey(self):
        """
        Test starting and stopping a journey.
        """
        # Verify if the journey starts and stops correctly
        self.assertFalse(self.pi.journey_started)
        self.pi.start_journey()
        self.assertTrue(self.pi.journey_started)
        # Try to start an already started journey
        self.pi.start_journey()  # Journey already started
        self.pi.stop_journey()
        self.assertFalse(self.pi.journey_started)
        # Try to stop a journey that isn't started
        self.pi.stop_journey()  # No journey in progress

class TestDriverlessCar(unittest.TestCase):
    """
    Unit test case for testing the DriverlessCar class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the DriverlessCar instance.
        """
        self.car = DriverlessCar('Model S', 10.0)

    def test_initialization(self):
        """
        Test the initialization of the DriverlessCar instance.
        """
        # Verify if the car attributes are set correctly
        self.assertEqual(self.car.carModel, 'Model S')
        self.assertEqual(self.car.carSpeed, 10.0)
        self.assertEqual(self.car.steeringAngle, 0.0)

    def test_set_and_get_car_speed(self):
        """
        Test setting and getting the car speed.
        """
        # Set the car speed and verify if it's set correctly
        self.car.set_car_speed(15.0)
        self.assertEqual(self.car.get_car_speed(), 15.0)

    def test_set_and_get_steering_angle(self):
        """
        Test setting and getting the steering angle.
        """
        # Set the steering angle and verify if it's set correctly
        self.car.set_steering_angle(30.0)
        self.assertEqual(self.car.get_steering_angle(), 30.0)

    def test_apply_brake(self):
        """
        Test applying the brake to stop the car.
        """
        # Apply brake and verify if the car speed is set to 0
        self.car.apply_brake()
        self.assertEqual(self.car.get_car_speed(), 0)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
