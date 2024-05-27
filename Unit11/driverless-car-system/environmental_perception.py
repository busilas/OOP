from sensors import Lidar, GPS, Camera

class EnvironmentalPerception:
    """
    Class representing environmental perception using sensors.

    Attributes:
        lidarSensor (Lidar): The Lidar sensor instance.
        gps (GPS): The GPS sensor instance.
        camera (Camera): The camera instance.
        sensorData (dict): Dictionary to store sensor data.
        obstacles (list): List to store detected obstacles.
    """
    def __init__(self):
        """
        Initializes an EnvironmentalPerception instance with sensor objects and data storage.
        """
        self.lidarSensor = Lidar()
        self.gps = GPS()
        self.camera = Camera()
        self.sensorData = {}
        self.obstacles = []

    def processSensorData(self):
        """
        Processes sensor data from Lidar, GPS, and Camera.

        Reads Lidar sensor data, obtains GPS coordinates, and captures an image using the camera.
        """
        lidarData = self.lidarSensor.readSensorData()
        gpsData = self.gps.getCoordinates()
        cameraImage = self.camera.captureImage()

        self.sensorData = {
            "lidar": lidarData,
            "gps": gpsData,
            "camera": cameraImage
        }

    def detectObstacles(self):
        """
        Detects obstacles based on Lidar sensor data.

        Filters Lidar distances to identify obstacles within a certain range.
        """
        if "lidar" in self.sensorData:
            lidarDistances = self.sensorData["lidar"]["data"]
            self.obstacles = [distance for distance in lidarDistances if distance < 10.0]
        else:
            self.obstacles = []

    def assessObstacleRisk(self):
        """
        Assesses obstacle risk based on detected obstacles.

        Returns:
            str: A message indicating whether high risk is detected or no obstacles are present.
        """
        if self.obstacles:
            return "High risk detected. Avoidance maneuver required."
        else:
            return "No obstacles detected."

    def getObstacles(self):
        """
        Returns the list of detected obstacles.

        Returns:
            list: List of obstacles detected by the Lidar sensor.
        """
        return self.obstacles
