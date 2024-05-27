import unittest
import random

from sensors import Lidar, Camera, GPS

class TestLidar(unittest.TestCase):
    """
    Unit test case for testing the Lidar class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the Lidar instance.
        """
        self.lidar = Lidar()

    def test_lidar_initialization(self):
        """
        Test the initialization of the Lidar instance.
        """
        # Verify if the sensor type is correctly set to "Lidar"
        self.assertEqual(self.lidar.sensorType, "Lidar")

    def test_lidar_readSensorData(self):
        """
        Test the readSensorData method of the Lidar class.
        """
        # Read sensor data from the Lidar instance
        data = self.lidar.readSensorData()
        # Check if the data dictionary contains the correct keys
        self.assertIn("sensor_type", data)
        self.assertIn("data", data)
        # Verify if the sensor type in the data is "Lidar"
        self.assertEqual(data["sensor_type"], "Lidar")
        # Verify if the data array has 360 points
        self.assertEqual(len(data["data"]), 360)
        # Verify if all points in the data array are within the expected range
        self.assertTrue(all(0.0 <= point <= 20.0 for point in data["data"]))

class TestCamera(unittest.TestCase):
    """
    Unit test case for testing the Camera class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the Camera instance.
        """
        self.camera = Camera()

    def test_camera_initialization(self):
        """
        Test the initialization of the Camera instance.
        """
        # Verify if the camera type is correctly set to "RGB"
        self.assertEqual(self.camera.cameraType, "RGB")

    def test_camera_captureImage(self):
        """
        Test the captureImage method of the Camera class.
        """
        # Capture an image using the Camera instance
        image = self.camera.captureImage()
        # Check if the image dictionary contains the correct keys
        self.assertIn("camera_type", image)
        self.assertIn("image", image)
        # Verify if the camera type in the image data is "RGB"
        self.assertEqual(image["camera_type"], "RGB")
        # Verify if the captured image data is "captured_image"
        self.assertEqual(image["image"], "captured_image")

class TestGPS(unittest.TestCase):
    """
    Unit test case for testing the GPS class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the GPS instance.
        """
        self.gps = GPS()

    def test_gps_initialization(self):
        """
        Test the initialization of the GPS instance.
        """
        # Verify if the initial latitude and longitude are set to 0.0
        self.assertEqual(self.gps.latitude, 0.0)
        self.assertEqual(self.gps.longitude, 0.0)

    def test_gps_getCoordinates(self):
        """
        Test the getCoordinates method of the GPS class.
        """
        # Get the coordinates from the GPS instance and verify the values
        coordinates = self.gps.getCoordinates()
        self.assertEqual(coordinates, (0.0001, 0.0001))
        # Get the coordinates again and verify the updated values
        coordinates = self.gps.getCoordinates()
        self.assertEqual(coordinates, (0.0002, 0.0002))

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
