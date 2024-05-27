import unittest
from unittest.mock import MagicMock, patch
from passenger_interaction import DriverlessCar
from environmental_perception import EnvironmentalPerception
from navigation import Navigation
from control import Control

class TestControl(unittest.TestCase):
    """
    Unit test class for the Control module of a driverless car.
    """

    def setUp(self):
        """
        Set up the test case with a DriverlessCar and Control instance.
        """
        self.vehicle = DriverlessCar('ModelX', 50.0)
        self.control = Control(self.vehicle)

    def test_accelerate(self):
        """
        Test the accelerate method to ensure it increases speed correctly and handles invalid input.
        """
        # Accelerate by 10.0 units and check the current speed
        self.control.accelerate(10.0)
        self.assertEqual(self.control.current_speed, 10.0)
        
        # Test acceleration with negative value which should raise a ValueError
        with self.assertRaises(ValueError):
            self.control.accelerate(-5.0)

    def test_brake(self):
        """
        Test the brake method to ensure it decreases speed correctly and handles invalid input.
        """
        # Accelerate to 10.0 units and then brake by 5.0 units
        self.control.accelerate(10.0)
        self.control.brake(5.0)
        self.assertEqual(self.control.current_speed, 5.0)
        
        # Brake by more than the current speed should set speed to 0
        self.control.brake(10.0)
        self.assertEqual(self.control.current_speed, 0.0)
        
        # Test braking with negative value which should raise a ValueError
        with self.assertRaises(ValueError):
            self.control.brake(-5.0)

    def test_steer(self):
        """
        Test the steer method to ensure it changes the steering angle correctly and handles invalid input.
        """
        # Steer to an angle of 15.0 degrees and check the steering angle
        self.control.steer(15.0)
        self.assertEqual(self.control.steering_angle, 15.0)
        
        # Test steering beyond the valid range which should raise a ValueError
        with self.assertRaises(ValueError):
            self.control.steer(45.0)
        
        with self.assertRaises(ValueError):
            self.control.steer(-45.0)

    @patch.object(DriverlessCar, 'set_car_speed')
    @patch.object(DriverlessCar, 'set_steering_angle')
    def test_updateVehicleDynamics(self, mock_set_steering_angle, mock_set_car_speed):
        """
        Test the updateVehicleDynamics method to ensure it updates the vehicle's speed and steering angle correctly.
        """
        # Set current speed and steering angle
        self.control.current_speed = 25.0
        self.control.steering_angle = 10.0
        # Update vehicle dynamics
        self.control.updateVehicleDynamics()
        
        # Check that set_car_speed and set_steering_angle were called with the correct values
        mock_set_car_speed.assert_called_once_with(25.0)
        mock_set_steering_angle.assert_called_once_with(10.0)

    @patch.object(EnvironmentalPerception, 'processSensorData')
    def test_updateSensorData(self, mock_processSensorData):
        """
        Test the updateSensorData method to ensure it processes sensor data correctly.
        """
        # Update sensor data
        self.control.updateSensorData()
        # Check that processSensorData was called once
        mock_processSensorData.assert_called_once()

    @patch.object(EnvironmentalPerception, 'assessObstacleRisk', return_value="High risk detected. Avoidance maneuver required.")
    @patch.object(EnvironmentalPerception, 'detectObstacles')
    def test_detectAndAvoidObstacles_high_risk(self, mock_detectObstacles, mock_assessObstacleRisk):
        """
        Test the detectAndAvoidObstacles method to ensure it handles high risk obstacles correctly.
        """
        # Detect and avoid obstacles
        self.control.detectAndAvoidObstacles()
        # Check that detectObstacles and assessObstacleRisk were called once
        mock_detectObstacles.assert_called_once()
        mock_assessObstacleRisk.assert_called_once()
        # Ensure the vehicle stops and sets a specific steering angle on high risk detection
        self.assertEqual(self.control.current_speed, 0.0)
        self.assertEqual(self.control.steering_angle, 10.0)

    @patch.object(Navigation, 'plan_route')
    def test_navigate(self, mock_plan_route):
        """
        Test the navigate method to ensure it plans a route correctly.
        """
        # Define start and destination points
        start = (0.0, 0.0)
        destination = (1.0, 1.0)
        # Navigate from start to destination
        self.control.navigate(start, destination)
        # Check that plan_route was called with the correct start and destination points
        mock_plan_route.assert_called_once_with(start, destination)

    @patch.object(Navigation, 'get_next_waypoint', side_effect=[(0.001, 0.001), None])
    @patch.object(Navigation, 'has_reached_destination', side_effect=[False, True])
    @patch.object(Navigation, 'calculate_distance', return_value=0.002)
    @patch.object(EnvironmentalPerception, 'processSensorData')
    @patch.object(EnvironmentalPerception, 'detectObstacles')
    def test_follow_route(self, mock_detectObstacles, mock_processSensorData, mock_calculate_distance, mock_has_reached_destination, mock_get_next_waypoint):
        """
        Test the follow_route method to ensure it follows the route correctly and handles reaching the destination.
        """
        # Mock the environmental perception's GPS to return a fixed coordinate
        self.control.environmentalPerception = MagicMock()
        self.control.environmentalPerception.gps.getCoordinates.return_value = (0.0, 0.0)
        # Follow the route
        self.control.follow_route()
        # Check the call count for has_reached_destination and calculate_distance
        self.assertEqual(mock_has_reached_destination.call_count, 2)  
        self.assertEqual(mock_calculate_distance.call_count, 1)

if __name__ == '__main__':
    unittest.main()
