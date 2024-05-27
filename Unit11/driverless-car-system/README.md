<h1 align = "center"> Driverless car system implementation </h1>

<br>
<br>




This repository contains a Python-based simulation of a driverless car system, leveraging Object-Oriented Programming (OOP) principles. The system integrates crucial components such as environmental perception, passenger interaction, vehicle control, and navigation to demonstrate their collaboration in delivering a seamless and safe driving experience within a simulated environment.

## Getting Started

To get started with the Driverless Car System, follow these steps:

1.	Clone the repository:

```bash
git clone https://github.com/busilas/OOP_UoE/tree/main/Unit11/driverless-car-system
```

2.	Navigate to the Project Directory:

```bash
cd driverless-car-system
```
    
3.	Run the application:

```bash
python main.py
```

Interact with the system by following the prompts to log in, sign up, and navigate the
car. Set destinations, initiate and halt journeys, and observe the vehicle's behavior.

## Project Structure

The project is organized into several modules, each responsible for different aspects
of the system:

**1.	sensors.py** module simulates various sensors used in the driverless car, including Lidar,
Camera, and GPS.

**Lidar** generates random distance data to represent a 360-degree scan.

Attributes:
- **sensorType:** set to "Lidar".
  
Methods:
- **readSensorData():** returns a dictionary with 360 random distances.

**Camera** simulates an RGB camera.

Attributes:

- **cameraType:** set to "RGB".
  
Methods:

- **captureImage():** returns a dictionary with the camera type and a placeholder for the captured image.

**GPS** simulates a GPS sensor.

Attributes:

- **latitude:** Latitude coordinate.
- **longitude:** Longitude coordinate.

Methods:

- **getCoordinates():** returns the current coordinates, incrementing them slightly each call to simulate movement.

**2.	environment_perception.py** processes data from sensors and detects obstacles.

**EnvironmentalPerception** integrates Lidar, GPS, and Camera sensors.

Attributes:

- **lidarSensor, gps, camera:** instances of Lidar, GPS, and Camera classes.
- **sensorData:** dictionary to store sensor data.
- **obstacles:** list of detected obstacles.
  
Methods:

-	**processSensorData():** reads data from all sensors and stores it in sensorData.
-	**detectObstacles():** detects obstacles based on Lidar data.
-	**assessObstacleRisk():** assesses the risk of detected obstacles.
-	**getObstacles():** returns the list of detected obstacles.

**3.	passenger_interaction.py** handles user interactions and passenger-related functionalities.

**User** represents a user with attributes for first name, last name, account name, and password.

Methods:

-	**verify_password(password):** verifies the provided password.

**PassengerInteraction** manages destinations and journey status.

Attributes:

-	**destinations:** dictionary of destinations.
-	**journey_started:** boolean indicating if a journey is in progress.

Methods:

- **set_destination(location, destination):** sets a destination for a location.
-	**search_destination(location):** searches for a destination by location.
-	**edit_destination(location, new_destination):** edits a destination.
-	**delete_destination(location):** deletes a destination.
-	**start_journey(), stop_journey():** manage journey status.

**DriverlessCar** simulates a driverless car.

Attributes:

-	**carModel:** model of the car.
-	**carSpeed:** speed of the car.
-	**steeringAngle:** steering angle of the car.

Methods:

-	**set_car_speed(speed), get_car_speed():** manage car speed.
-	**set_steering_angle(angle), get_steering_angle():** manage steering angle.
-	**apply_brake():** stops the car.

**4.	driverless_car_system.py** integrates user management and passenger interaction into the main system.

**DriverlessCarSystem** manages user accounts and their interactions with the system.

Attributes:

-	**users:** list of registered users.
-	**passenger_interaction:** instance of PassengerInteraction.
-	**current_user:** currently logged-in user.

Methods:

-	**login(), logout(), signup():** manage user sessions.
-	**user_menu(), main_menu():** display menus for user interactions.

**5.	navigation.py** handles route planning and navigation.

**Navigation** manages route planning and waypoint navigation.

Attributes:

-	**route:** list of waypoints forming the route.
-	**current_index:** index of the current waypoint.

Methods:

-	**plan_route(start, destination):** plans a route from start to destination.
- **get_next_waypoint():** returns the next waypoint.
-	**has_reached_destination():** checks if the destination has been reached.
- **calculate_distance(point1, point2):** calculates the distance between two points.

**6.	control.py** controls the vehicle based on sensor data and navigation.

**Control** manages vehicle speed and steering to avoid obstacles and follow a route.

Attributes:

-	**vehicle:** instance of DriverlessCar.
-	**environmentalPerception:** instance of EnvironmentalPerception.
-	**navigation:** instance of Navigation.
-	**current_speed:** current speed of the vehicle.
-	**steering_angle:** current steering angle of the vehicle.

Methods:

- **accelerate(acceleration), brake(deceleration), steer(steering_angle):** manage vehicle dynamics.
- **updateVehicleDynamics():** updates vehicle speed and steering angle.
- **updateSensorData():** updates sensor data.
- **detectAndAvoidObstacles():** detects and avoids obstacles.
- **navigate(start, destination):** plans a route and starts navigation.
- **follow_route():** follows the planned route.

**7.	main.py** - the entry point of the application.

**main()** initializes the DriverlessCar and Control instances. Demonstrates the usage of navigation and control functionalities.


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


