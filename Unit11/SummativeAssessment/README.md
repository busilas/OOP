<h1 align = "center"> Driverless car system implementation </h1>

<br>



## Overview

This repository contains a Python OOP-based simulation of a driverless car system implementation. The system is a comprehensive simulation framework that integrates key components, such as environmental perception, passenger interaction, vehicle control, and navigation, to demonstrate how these components collaborate to deliver a seamless and safe driving experience in a simulated environment.

## Getting Started

To get started with the Driverless Car System, follow these steps:

1.	Clone the repository:

```bash
git clone https://github.com/busilas/driverless-car-system.git
```

2.	Navigate to the Project Directory:

```bash
cd driverless-car-system
```
    
3.	Run the application:

```bash
python main.py
```

## Interact with the system:

Follow the prompts to log in, sign up, and interact with the car system.

Set destinations, start and stop journeys, and observe the vehicle's behavior.

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

**3.	passenger_interaction.py** this module handles user interactions and passenger-related functionalities.

**User** represents a user with attributes for first name, last name, account name, and password.

Methods:

-	**verify_password(password):** Verifies the provided password.

**PassengerInteraction** manages destinations and journey status.

Attributes:

-	**destinations:** Dictionary of destinations.
-	**journey_started:** Boolean indicating if a journey is in progress.

Methods:

- **set_destination(location, destination):** Sets a destination for a location.
-	**search_destination(location):** Searches for a destination by location.
-	**edit_destination(location, new_destination):** Edits a destination.
-	**delete_destination(location):** Deletes a destination.
-	**start_journey(), stop_journey():** Manage journey status.

**DriverlessCar** simulates a driverless car.

Attributes:

-	**carModel:** Model of the car.
-	**carSpeed:** Speed of the car.
-	**steeringAngle:** Steering angle of the car.

Methods:

-	**set_car_speed(speed), get_car_speed():** Manage car speed.
-	**set_steering_angle(angle), get_steering_angle():** Manage steering angle.
-	**apply_brake():** Stops the car.

**4.	driverless_car_system.py** this module integrates user management and passenger interaction into the main system.

**DriverlessCarSystem** manages user accounts and their interactions with the system.

Attributes:

-	**users:** List of registered users.
-	**passenger_interaction:** Instance of PassengerInteraction.
-	**current_user:** Currently logged-in user.

Methods:

-	**login(), logout(), signup():** Manage user sessions.
-	**user_menu(), main_menu():** Display menus for user interactions.

**5.	navigation.py** this module handles route planning and navigation.

**Navigation** manages route planning and waypoint navigation.

Attributes:

-	**route:** List of waypoints forming the route.
-	**current_index:** Index of the current waypoint.

Methods:

-	**plan_route(start, destination):** Plans a route from start to destination.
- **get_next_waypoint():** Returns the next waypoint.
-	**has_reached_destination():** Checks if the destination has been reached.
- **calculate_distance(point1, point2):** Calculates the distance between two points.

**6.	control.py** this module controls the vehicle based on sensor data and navigation.

**Control** manages vehicle speed and steering to avoid obstacles and follow a route.

Attributes:

-	**vehicle:** Instance of DriverlessCar.
-	**environmentalPerception:** Instance of EnvironmentalPerception.
-	**navigation:** Instance of Navigation.
-	**current_speed:** Current speed of the vehicle.
-	**steering_angle:** Current steering angle of the vehicle.

Methods:

- **accelerate(acceleration), brake(deceleration), steer(steering_angle):** Manage vehicle dynamics.
- **updateVehicleDynamics():** Updates vehicle speed and steering angle.
- **updateSensorData():** Updates sensor data.
- **detectAndAvoidObstacles():** Detects and avoids obstacles.
- **navigate(start, destination):** Plans a route and starts navigation.
- **follow_route():** Follows the planned route.

**7.	main.py** - the entry point of the application.

**main()** initializes the DriverlessCar and Control instances. Demonstrates the usage of navigation and control functionalities.



-	**processSensorData():** Reads data from all sensors and stores it in sensorData.
-	**detectObstacles():** Detects obstacles based on Lidar data.
-	**assessObstacleRisk():** Assesses the risk of detected obstacles.
-	**getObstacles():** Returns the list of detected obstacles.

## Future Enhancements

This project can be extended in several ways:

-	Improved Sensor Simulations: Implement more realistic sensor data generation.
-	Advanced Navigation Algorithms: Use real mapping data and more complex pathfinding algorithms.
-	User Interface: Develop a graphical user interface for easier interaction.
-	Machine Learning Integration: Incorporate machine learning for better obstacle detection and avoidance.

## Conclusion

The Driverless Car System is a foundational framework for simulating and understanding the complexities involved in driverless car technologies. By integrating various modules for environmental perception, passenger interaction, vehicle control, and navigation, this project provides a comprehensive overview of how driverless cars operate and make decisions in real time.


<br>

## Reference list

Lopez, E. (2022) Bubble sort - how it works, Psuedocode and C++ & Python implementation, Medium. Available at: https://medium.com/codex/bubble-sort-how-it-works-psuedocode-and-c-python-implementation-c45306d44827 [Accessed: 27 January 2024]. 

