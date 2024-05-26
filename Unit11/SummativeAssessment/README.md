<h1 align = "center"> Driverless car system implementation </h1>



This repository contains a Python OOP-based simulation of a driverless car system implementation. It encompasses classes that represent various elements of the system, such as user, vehicle, navigation, sensors, and more.

## Overview

The Driverless Car System is a comprehensive simulation framework that integrates key components, such as environmental perception, passenger interaction, vehicle control, and navigation, to demonstrate how these components collaborate to deliver a seamless and safe driving experience in a simulated environment.

## Project Structure

The project is organized into several modules, each responsible for different aspects of the system. Below is a detailed description of each module:

**1.	sensors.py** this module contains classes that simulate various sensors used in the driverless car, including Lidar, Camera, and GPS.

**Lidar** simulates a Lidar sensor by generating random distance data to represent a 360-degree scan.

Attributes:
- **sensorType:** Type of the sensor, set to "Lidar".
  
Methods:
- **readSensorData():** Returns a dictionary with sensor data, including 360 random distances.

**Camera** simulates an RGB camera.

Attributes:

- **cameraType:** Type of the camera, set to "RGB".
  
Methods:

- **captureImage():** Returns a dictionary with the camera type and a placeholder for the captured image.

**GPS** simulates a GPS sensor.

Attributes:

- **latitude:** Latitude coordinate.
- **longitude:** Longitude coordinate.

Methods:

- **getCoordinates():** Returns the current coordinates, incrementing them slightly each call to simulate movement.

**2.	environment_perception.py** this module is responsible for processing data from the sensors and detecting obstacles.

**EnvironmentalPerception** integrates Lidar, GPS, and Camera sensors to form a comprehensive perception system.

Attributes:

- **lidarSensor, gps, camera:** Instances of Lidar, GPS, and Camera classes.
-	**sensorData:** Dictionary to store sensor data.
- **obstacles:** List of detected obstacles.
  
Methods:

-	**processSensorData():** Reads data from all sensors and stores it in sensorData.
-	**detectObstacles():** Detects obstacles based on Lidar data.
-	**assessObstacleRisk():** Assesses the risk of detected obstacles.
-	**getObstacles():** Returns the list of detected obstacles.

