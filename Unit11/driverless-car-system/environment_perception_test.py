import unittest
import random
from unittest.mock import MagicMock
from environmental_perception import EnvironmentalPerception
from sensors import Lidar, GPS, Camera

class TestEnvironmentalPerception(unittest.TestCase):
    """
    Unit test class for the EnvironmentalPerception class.
    """

    def setUp(self):
        """
        Set up the test case with an instance of EnvironmentalPerception.
        Mocks the sensor data for Lidar, GPS, and Camera.
        """
        self.env_perception = EnvironmentalPerception()
        
        # Mock Lidar sensor data with random values between 0.0 and 20.0
        self.env_perception.lidarSensor.readSensorData = MagicMock(return_value={
            "sensor_type": "Lidar",
            "data": [random.uniform(0.0, 20.0) for _ in range(360)]
        })
        
        # Mock GPS coordinates to a fixed location (Los Angeles coordinates)
        self.env_perception.gps.getCoordinates = MagicMock(return_value=(34.052235, -118.243683))
        
        # Mock camera capture image data
        self.env_perception.camera.captureImage = MagicMock(return_value={"camera_type": "RGB", "image": "captured_image"})

    def test_initialization(self):
        """
        Test the initialization of the EnvironmentalPerception instance.
        """
        # Verify the types of sensors initialized
        self.assertIsInstance(self.env_perception.lidarSensor, Lidar)
        self.assertIsInstance(self.env_perception.gps, GPS)
        self.assertIsInstance(self.env_perception.camera, Camera)
        
        # Verify initial sensor data and obstacles
        self.assertEqual(self.env_perception.sensorData, {})
        self.assertEqual(self.env_perception.obstacles, [])

    def test_processSensorData(self):
        """
        Test the processSensorData method to ensure sensor data is processed correctly.
        """
        # Process sensor data
        self.env_perception.processSensorData()
        
        # Verify sensor data contains entries for Lidar, GPS, and Camera
        self.assertIn("lidar", self.env_perception.sensorData)
        self.assertIn("gps", self.env_perception.sensorData)
        self.assertIn("camera", self.env_perception.sensorData)
        
        # Verify GPS and Camera data matches mocked values
        self.assertEqual(self.env_perception.sensorData["gps"], (34.052235, -118.243683))
        self.assertEqual(self.env_perception.sensorData["camera"], {"camera_type": "RGB", "image": "captured_image"})

    def test_detectObstacles(self):
        """
        Test the detectObstacles method to ensure obstacles are detected correctly.
        """
        # Process sensor data and detect obstacles
        self.env_perception.processSensorData()
        self.env_perception.detectObstacles()
        
        # Verify obstacles list is created
        self.assertIsInstance(self.env_perception.obstacles, list)
        
        # Verify all detected obstacles are within 10.0 units
        for obstacle in self.env_perception.obstacles:
            self.assertLess(obstacle, 10.0)

    def test_assessObstacleRisk(self):
        """
        Test the assessObstacleRisk method to ensure it assesses obstacle risks correctly.
        """
        # Process sensor data and detect obstacles
        self.env_perception.processSensorData()
        self.env_perception.detectObstacles()
        
        # Assess obstacle risk based on detected obstacles
        if self.env_perception.obstacles:
            self.assertEqual(self.env_perception.assessObstacleRisk(), "High risk detected. Avoidance maneuver required.")
        else:
            self.assertEqual(self.env_perception.assessObstacleRisk(), "No obstacles detected.")

    def test_getObstacles(self):
        """
        Test the getObstacles method to ensure it retrieves the detected obstacles correctly.
        """
        # Process sensor data and detect obstacles
        self.env_perception.processSensorData()
        self.env_perception.detectObstacles()
        
        # Retrieve obstacles and verify they match the detected obstacles
        obstacles = self.env_perception.getObstacles()
        self.assertEqual(obstacles, self.env_perception.obstacles)

if __name__ == '__main__':
    unittest.main()
