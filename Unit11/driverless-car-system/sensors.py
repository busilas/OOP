import random

class Lidar:
    """
    Represents a Lidar sensor used for environmental perception.

    Attributes:
        sensorType (str): The type of sensor, which is Lidar.
    """
    def __init__(self):
        """
        Initializes a LidarSensor instance.
        """
        self.sensorType = "Lidar"

    def readSensorData(self):
        """
        Simulates reading Lidar sensor data.

        Returns:
            dict: A dictionary containing Lidar sensor data with sensor type and data.
        """
        lidarData = {
            "sensor_type": self.sensorType,
            "data": [random.uniform(0.0, 20.0) for _ in range(360)]  # Simulate 360-degree Lidar scan
        }
        return lidarData


class Camera:
    """
    Represents a camera used for capturing images.

    Attributes:
        cameraType (str): The type of camera, which is RGB.
    """
    def __init__(self):
        """
        Initializes a Camera instance.
        """
        self.cameraType = "RGB"

    def captureImage(self):
        """
        Simulates capturing an image using the specified camera type.

        Returns:
            dict: A dictionary containing the camera type and the captured image.
        """
        return {"camera_type": self.cameraType, "image": "captured_image"}


class GPS:
    """
    Represents a GPS sensor used for obtaining coordinates.

    Attributes:
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.
    """
    def __init__(self):
        """
        Initializes a GPS instance with initial latitude and longitude set to zero.
        """
        self.latitude = 0.0
        self.longitude = 0.0

    def getCoordinates(self):
        """
        Simulates GPS providing coordinates.

        Returns:
            tuple: A tuple containing latitude and longitude coordinates.
        """
        self.latitude += 0.0001  # Increment latitude for simulation
        self.longitude += 0.0001  # Increment longitude for simulation
        return (self.latitude, self.longitude)
